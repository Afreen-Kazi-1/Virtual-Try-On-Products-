import os
import json
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers

# Load Image Function
def load_image(image_path):
    image = tf.io.read_file(image_path)
    image = tf.image.decode_png(image, channels=3)
    image = tf.image.resize(image, (256, 256))
    image = image / 255.0  # Normalize to [0,1]
    return image

# Load Control Points Function
def load_control_points(points_path):
    with open(points_path, 'r') as f:
        points_data = json.load(f)
    points = np.array(points_data)
    return tf.convert_to_tensor(points, dtype=tf.float32)

# Create Dataset
def create_dataset(images_path, control_points_path, batch_size=16):
    image_files = sorted([os.path.join(images_path, file) for file in os.listdir(images_path)])
    control_point_files = sorted([os.path.join(control_points_path, file) for file in os.listdir(control_points_path)])
    
    dataset = tf.data.Dataset.from_tensor_slices((image_files, control_point_files))
    dataset = dataset.map(lambda img, pts: (load_image(img), load_control_points(pts)), num_parallel_calls=tf.data.AUTOTUNE)
    dataset = dataset.shuffle(buffer_size=1000).batch(batch_size).prefetch(tf.data.AUTOTUNE)
    return dataset

# Custom Sampling Function
def bilinear_sampler(imgs, grids):
    """Performs bilinear sampling of the input images according to the grid coordinates."""
    def _interpolate(im, x, y):
        # Grid coordinates
        x0 = tf.floor(x)
        x1 = x0 + 1
        y0 = tf.floor(y)
        y1 = y0 + 1

        # Clip values to be in range
        max_x = tf.cast(tf.shape(im)[2] - 1, 'float32')
        max_y = tf.cast(tf.shape(im)[1] - 1, 'float32')
        x0 = tf.clip_by_value(x0, 0., max_x)
        x1 = tf.clip_by_value(x1, 0., max_x)
        y0 = tf.clip_by_value(y0, 0., max_y)
        y1 = tf.clip_by_value(y1, 0., max_y)

        # Cast to int
        x0 = tf.cast(x0, 'int32')
        x1 = tf.cast(x1, 'int32')
        y0 = tf.cast(y0, 'int32')
        y1 = tf.cast(y1, 'int32')

        # Gather pixel values
        Ia = tf.gather_nd(im, tf.stack([y0, x0], axis=-1))
        Ib = tf.gather_nd(im, tf.stack([y1, x0], axis=-1))
        Ic = tf.gather_nd(im, tf.stack([y0, x1], axis=-1))
        Id = tf.gather_nd(im, tf.stack([y1, x1], axis=-1))

        # Compute weights
        wa = (x1 - x) * (y1 - y)
        wb = (x1 - x) * (y - y0)
        wc = (x - x0) * (y1 - y)
        wd = (x - x0) * (y - y0)

        # Add weighted pixels
        out = tf.add_n([wa * Ia, wb * Ib, wc * Ic, wd * Id])
        return out

    x = grids[:, :, :, 0]
    y = grids[:, :, :, 1]
    print("Sampler ran")

    return _interpolate(imgs, x, y)

# Localization Network
def localization_network(ip_shape=(256, 256, 3), num_control_points=12):
    inputs = tf.keras.Input(shape=ip_shape)

    x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(inputs)
    x = layers.MaxPooling2D(pool_size=(2, 2))(x)

    x = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(x)
    x = layers.MaxPooling2D(pool_size=(2, 2))(x)

    x = layers.Conv2D(128, (3, 3), activation='relu', padding='same')(x)
    x = layers.MaxPooling2D(pool_size=(2, 2))(x)

    x = layers.Flatten()(x)
    x = layers.Dense(256, activation='relu')(x)

    # Output should match the number of control points * 4
    output = layers.Dense(num_control_points * 4, activation='linear')(x)
    output = layers.Reshape((num_control_points, 4))(output)

    model = tf.keras.Model(inputs, output)
    print("locnet ran")
    return model


# Grid Generator
class GridGenerator(layers.Layer):
    def __init__(self):
        super(GridGenerator, self).__init__()

    def call(self, control_points, transparams):
        # Debugging info: Print the shapes of inputs
        print(f"control_points shape: {control_points.shape}")
        print(f"transparams shape: {transparams.shape}")
        
        # Ensure transparams has the correct shape: [batch_size, num_control_points, at least 4]
        if transparams.shape[-1] < 4:
            raise ValueError(f"transparams must have at least 4 dimensions, but got {transparams.shape[-1]} dimensions.")

        # Compute distances between control points and transformation parameters
        r = tf.norm(control_points[:, None, :] - transparams[:, :, None, :2], axis=-1)
        
        # Kernel matrix
        K = r ** 2 * tf.math.log(r + 1e-6)
        
        # Linear part of transformation: Only consider the non-affine part of the transformation
        transformed_points = tf.matmul(K, transparams[:, :, 2:4])
        
        # Add the affine part of the transformation
        transformed_points = control_points[:, :, :2] + transformed_points
        print("grid gen ran")
        return transformed_points



# Combine STN Components
def STN(ip_image, control_points, ip_shape=(256, 256, 3), num_control_points=12):
    loc_net = localization_network(ip_shape=ip_shape, num_control_points=num_control_points)
    transformation_params = loc_net(ip_image)
    grid_generator_layer = GridGenerator()
    grid = grid_generator_layer(control_points, transformation_params)
    print("grid found")
    output_image = bilinear_sampler(ip_image, grid)
    print("stn compiled")
    return output_image


# Model Definition
input_image = tf.keras.Input(shape=(256, 256, 3))
control_points = tf.keras.Input(shape=(12, 2))  # Example control points shape
output_image = STN(input_image, control_points, ip_shape=(256, 256, 3), num_control_points = 12)
model = tf.keras.Model(inputs=[input_image, control_points], outputs=output_image)

# Compile the Model
model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])

# Train the Model
batch_size = 100
train_dataset = create_dataset(train_images_path, train_control_points_path, batch_size=batch_size)
test_dataset = create_dataset(test_images_path, test_control_points_path, batch_size=batch_size)
epochs = 20  # Adjust as needed
history = model.fit(train_dataset, validation_data=test_dataset, epochs=epochs)

# Evaluate on the Test Set
test_loss, test_accuracy = model.evaluate(test_dataset)
print(f'Test Loss: {test_loss}')
print(f'Test Accuracy: {test_accuracy}')

# Save the Model
model.save('stn_warping_model.h5')
