# Object Detection

Object detection is a computer vision task that involves identifying and localizing objects within an image or video. Unlike image classification, which only predicts the class of the object present in an image, object detection provides both the class labels and the bounding boxes of the objects detected.

Bounding Boxes: Rectangular boxes that define the position and size of the objects in an image.

## Landmark Detection 
Landmark detection, also known as facial landmark detection when applied to faces, involves identifying key points in images that correspond to important features. These key points, or landmarks, are typically the eyes, nose, mouth, and other significant points on an object or face. Landmark detection is essential in various applications, including facial recognition, emotion detection, and augmented reality.

## Sliding window object detection 
Starts with smaller windows and then increase window size convolving each  window of the size

The convolutional implementation of sliding window object detection involves using a convolutional neural network (CNN) to detect objects within an image by applying a sliding window across different regions of the image. This approach leverages the convolution operation's inherent property of sharing weights across different regions, making the detection process more efficient.
