import tensorflow as tf
from tensorflow.keras import layers, models

def Unet(ip_shape, num_classes):
  input = layers.Input(ip_shape)

  conv1 = layers.Conv2D(64, (3,3), activation='relu', padding='same')(input)
  conv1 = layers.Conv2D(64, (3,3), activation='relu', padding='same')(conv1)
  pool1 = layers.MaxPooling2D(pool_size=(2,2))(conv1)

  conv2 = layers.Conv2D(128, (3,3), activation='relu', padding='same')(pool1)
  conv2 = layers.Conv2D(128, (3,3), activation='relu', padding='same')(conv2)
  pool2 = layers.MaxPooling2D(pool_size=(2,2))(conv2)

  conv3 = layers.Conv2D(256, (3,3), activation='relu', padding='same')(pool2)
  conv3 = layers.Conv2D(256, (3,3), activation='relu', padding='same')(conv3)
  pool3 = layers.MaxPooling2D(pool_size=(2,2))(conv3)

  conv4 = layers.Conv2D(512, (3,3), activation='relu', padding='same')(pool3)
  conv4 = layers.Conv2D(512, (3,3), activation='relu', padding='same')(conv4)
  pool4 = layers.MaxPooling2D(pool_size=(2,2))(conv4)

  ##Bottleneck

  conv5 = layers.Conv2D(1024, (3,3), activation='relu', padding='same')(pool4)
  conv5 = layers.Conv2D(1024, (3,3), activation='relu', padding='same')(conv5)

  conv6 = layers.Conv2DTranspose(512, (2,2), strides=(2,2), padding='same')(conv5)
  conv6 = layers.concatenate([conv6, conv4])
  conv6 = layers.Conv2D(512, (3,3), activation='relu', padding='same')(conv6)
  conv6 = layers.Conv2D(512, (3,3), activation='relu', padding='same')(conv6)

  conv7 = layers.Conv2DTranspose(256, (2,2), strides=(2,2), padding='same')(conv6)
  conv7 = layers.concatenate([conv7, conv3])
  conv7 = layers.Conv2D(256, (3,3), activation='relu', padding='same')(conv7)
  conv7 = layers.Conv2D(256, (3,3), activation='relu', padding='same')(conv7)

  conv8 = layers.Conv2DTranspose(128, (2,2), strides=(2,2), padding='same')(conv7)
  conv8 = layers.concatenate([conv8, conv2])
  conv8 = layers.Conv2D(128, (3,3), activation='relu', padding='same')(conv8)
  conv8 = layers.Conv2D(128, (3,3), activation='relu', padding='same')(conv8)

  conv9 = layers.Conv2DTranspose(64, (2,2), strides=(2,2), padding='same')(conv8)
  conv9 = layers.concatenate([conv9, conv1])
  conv9 = layers.Conv2D(64, (3,3), activation='relu', padding='same')(conv9)
  conv9 = layers.Conv2D(64, (3,3), activation='relu', padding='same')(conv9)

  output = layers.Conv2D(num_classes, (1,1), activation='softmax')(conv9)

  model = models.Model(inputs=input, outputs=output)
  return model

def mask_creation (im_shape, keypts):
  mask = np.zeros(im_shape)
  radius = 4
  for index,(x,y) in enumerate(keypts):
    cv2.circle(mask, (x,y), radius, (index+1), -1)
  return mask
