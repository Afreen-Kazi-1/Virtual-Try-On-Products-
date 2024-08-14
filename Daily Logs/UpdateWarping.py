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

# Load Mask Function
def load_mask(mask_path):
    mask = tf.io.read_file(mask_path)
    mask = tf.image.decode_png(mask, channels=1)  # Assuming the mask is grayscale
    mask = tf.image.resize(mask, (256, 256))
    mask = tf.cast(mask, tf.float32) / 255.0  # Normalize to [0,1]
    return mask

# Load Control Points Function
def load_control_points(points_path):
    # Use TensorFlow to read the file as a string
    points_string = tf.io.read_file(points_path)
    points_string = points_string.numpy().decode('utf-8')  # Convert to a regular string

    # Parse the JSON string
    points_dict = json.loads(points_string)

    # Extract pose keypoints and reshape to (num_keypoints, 3)
    keypoints = np.array(points_dict['people'][0].get('pose_keypoints', [])).reshape(-1, 3)

    # Select keypoints for the upper body (3 to 9, 12)
    selected_keypoints = keypoints[[3, 4, 5, 6, 7, 8, 9, 12], :2]

    # Convert to tensor
    points_tensor = tf.convert_to_tensor(selected_keypoints, dtype=tf.float32)

    return points_tensor


# Create Dataset
def create_dataset(image_folder, points_folder, mask_folder, batch_size):
    image_paths = [os.path.join(image_folder, img) for img in os.listdir(image_folder)]
    points_paths = [os.path.join(points_folder, pts) for pts in os.listdir(points_folder)]
    mask_paths = [os.path.join(mask_folder, msk) for msk in os.listdir(mask_folder)]
    
    def load_data(img_path, pts_path, msk_path):
        image = load_image(img_path)
        control_points = load_control_points(pts_path)
        mask = load_mask(msk_path)
        return image, control_points, mask

    dataset = tf.data.Dataset.from_tensor_slices((image_paths, points_paths, mask_paths))
    dataset = dataset.map(lambda img, pts, msk: load_data(img, pts, msk), num_parallel_calls=tf.data.AUTOTUNE)
    dataset = dataset.batch(batch_size)
    print("dataset created")
    return dataset

# Custom Sampling Function
class InterpolationLayer(layers.Layer):
    def __init__(self):
        super(InterpolationLayer, self).__init__()

    def call(self, inputs):
        imgs, x, y = inputs

        # Ensure x and y are within valid ranges
        x0 = tf.floor(x)
        x1 = x0 + 1
        y0 = tf.floor(y)
        y1 = y0 + 1

        max_x = tf.cast(tf.shape(imgs)[2] - 1, 'float32')
        max_y = tf.cast(tf.shape(imgs)[1] - 1, 'float32')
        x0 = tf.clip_by_value(x0, 0., max_x)
        x1 = tf.clip_by_value(x1, 0., max_x)
        y0 = tf.clip_by_value(y0, 0., max_y)
        y1 = tf.clip_by_value(y1, 0., max_y)

        x0 = tf.cast(x0, 'int32')
        x1 = tf.cast(x1, 'int32')
        y0 = tf.cast(y0, 'int32')
        y1 = tf.cast(y1, 'int32')

        # Gather pixel values
        indices_a = tf.stack([y0, x0], axis=-1)
        indices_b = tf.stack([y1, x0], axis=-1)
        indices_c = tf.stack([y0, x1], axis=-1)
        indices_d = tf.stack([y1, x1], axis=-1)

        Ia = tf.gather_nd(imgs, indices_a, batch_dims=1)
        Ib = tf.gather_nd(imgs, indices_b, batch_dims=1)
        Ic = tf.gather_nd(imgs, indices_c, batch_dims=1)
        Id = tf.gather_nd(imgs, indices_d, batch_dims=1)

        x0 = tf.cast(x0, 'float32')
        x1 = tf.cast(x1, 'float32')
        y0 = tf.cast(y0, 'float32')
        y1 = tf.cast(y1, 'float32')

        wa = (x1 - x) * (y1 - y)
        wb = (x1 - x) * (y - y0)
        wc = (x - x0) * (y1 - y)
        wd = (x - x0) * (y - y0)

        # Debugging: Print shapes before the weighted sum
        print(f"Ia shape: {Ia.shape}, wa shape: {wa.shape}")
        print(f"Ib shape: {Ib.shape}, wb shape: {wb.shape}")
        print(f"Ic shape: {Ic.shape}, wc shape: {wc.shape}")
        print(f"Id shape: {Id.shape}, wd shape: {wd.shape}")

        # Perform interpolation
        out = wa[:, :, None] * Ia + wb[:, :, None] * Ib + wc[:, :, None] * Ic + wd[:, :, None] * Id
        print("interpolated")
        return out


# Bilinear Sampling Function
def bilinear_sampler(imgs, grids):
    x = grids[:, :, 0]
    y = grids[:, :, 1]
    
    # Use the custom interpolation layer
    interpolation_layer = InterpolationLayer()
    print("sampling done")
    return interpolation_layer([imgs, x, y])

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
        transformed_points = control_points + transformed_points
        print("grid generated")
        return transformed_points

# Combine STN Components
def STN(ip_image, control_points, ip_shape=(256, 256, 3), num_control_points=12):
    loc_net = localization_network(ip_shape=ip_shape, num_control_points=num_control_points)
    transformation_params = loc_net(ip_image)
    grid_generator_layer = GridGenerator()
    grid = grid_generator_layer(control_points, transformation_params)
    output_image = bilinear_sampler(ip_image, grid)
    print("stn formed")
    return output_image

# Model Definition
input_image = tf.keras.Input(shape=(256, 256, 3))
control_points = tf.keras.Input(shape=(12, 2))  # Example control points shape
output_image = STN(input_image, control_points, ip_shape=(256, 256, 3), num_control_points=12)
model = tf.keras.Model(inputs=[input_image, control_points], outputs=output_image)
print("model defined")

# Compile the Model
model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])
print("model compiled")

# Train the Model
batch_size = 64 
train_dataset = create_dataset("train/cloth", "train/pose", "train/cloth-mask", batch_size=batch_size)
test_dataset = create_dataset("test/cloth", "test/pose", "test/cloth-mask", batch_size=batch_size)
epochs = 20  # Adjust as needed
history = model.fit(train_dataset, validation_data=test_dataset, epochs=epochs)
print("model trained")
# Evaluate on the Test Set
test_loss, test_accuracy = model.evaluate(test_dataset)
print(f'Test Loss: {test_loss}')
print(f'Test Accuracy: {test_accuracy}')

# Save the Model
model.save('stn_warping_model.h5')
