## Image classification and localization
label the image and also draw a bounding box ard it.

Network Architecture:
Starts with a ConvNet that processes the image and outputs features.
Includes a softmax unit to predict the class (e.g., pedestrian, car, motorcycle, background).

Bounding Box Prediction:
The network is modified to output additional values for the bounding box: 
bx,by,bh,bw.
These values represent the center coordinates (bx, by), height (bh), and width (bw) of the bounding box.
Coordinates are normalized: (0,0) for top-left and (1,1) for bottom-right.

Output Vector:

The network's output vector 
y consists of:
pc: Probability of there being an object (1 if object, 0 if background).
bx,by,bh,bw: Bounding box parameters if pc=1.
c1,c2,c3: Class probabilities for pedestrian, car, motorcycle respectively (if 

pc=1).

## landmark detection
Face Recognition:
Identify landmarks such as corners of the eyes.
Neural network outputs lx and ly for coordinates of specific points.
Example: For four corners of the eyes, network outputs l1x, l1y, l2x, l2y, etc.
Extended Landmarks:
Identify multiple points on a face, like key points along the eyes, mouth, and nose.
Example: Define 64 key points (landmarks) on a face to map features like the jawline and mouth shape.

## sliding window approach
Create a labeled training set with closely cropped examples of objects.
Pick a window size and move it across the test image.
Input each window region to the ConvNet to classify if it contains the object.
After sliding one window size across the image, repeat with larger windows.
Continue this process to cover various scales of the object in the image.
Challenges:
High computational cost due to numerous window regions.
Trade-off between stride size and detection accuracy:
Larger stride: Fewer windows but less accurate.
Smaller stride: More windows but higher computational cost.

we can follow convolutional implementation of sliding window approach
Instead of processing each window separately, the entire image is passed through a convolutional neural network (ConvNet) in one go

## YOLO alogorithm
YOLO stands for "You Only Look Once." It aims to make object detection faster and more accurate by treating it as a single regression problem, straight from image pixels to bounding box coordinates and class probabilities.
divides an input image into a grid and assigns each grid cell the responsibility of predicting bounding boxes and class probabilities for objects whose centers fall within the cell.

## IoU
The union is the total area covered by both the ground-truth and predicted bounding boxes. The intersection is the overlapping area shared by these two boxes.
The IoU is calculated by dividing the area of the intersection by the area of the union
This ratio measures how much the predicted box overlaps with the ground-truth box.
 By convention, if the IoU is greater than or equal to 0.5, the predicted bounding box is considered correct. This threshold can be adjusted (e.g., to 0.6 or 0.7) for more stringent evaluation.

## Non max suppression
Filter: Discard bounding boxes with confidence scores below a set threshold.
Select: Choose the bounding box with the highest confidence.
Suppress: Remove other boxes that overlap significantly (high IoU) with the selected box.
Repeat: Continue selecting and suppressing until all boxes are processed.

## anchor boxes
Anchor boxes help object detection by letting each grid cell use multiple pre-set shapes to match objects of different sizes. Each grid cell can then predict objects for each shape, so if two objects are in the same cell, it can handle both. 

YOLO ALGO USING ANCHOR BOX CONCEPT

Training: Train a neural network to predict the presence and location of objects in an image. Each grid cell in a grid outputs predictions for multiple anchor boxes. These predictions include the probability of an object, its bounding box, and its class.

Output: The network outputs a volume that includes predictions for each grid cell and anchor box. For instance, with two anchor boxes and a 3x3 grid, the output volume might be 3x3x2x8, representing the predicted bounding boxes and class probabilities.

Prediction: For a new image, the network predicts bounding boxes and their class probabilities for each grid cell. Non-max suppression is used to filter out low-probability detections and reduce multiple detections of the same object.

Non-Max Suppression: Apply this technique separately for each class to finalize object detections by removing overlapping bounding boxes based on their confidence scores.


## semantic segmentation
To classify each pixel in an image into predefined categories (e.g., car, building, road).

## transpose convolution
Transpose convolution, or deconvolution, is used to increase the spatial dimensions of an input image, often used in neural networks for tasks like semantic segmentation.

Watch vid for more clearance

## u net architecture
Encoder (Contracting Path): Uses standard convolutions to downsample the input image, compressing it into a smaller representation while capturing high-level features.

Decoder (Expansive Path): Uses transpose convolutions to upsample this compressed representation back to the original image size.

Skip Connections: Directly connect the corresponding layers of the encoder and decoder. These connections help combine the high-resolution, detailed information from the encoder with the high-level context from the decoder, improving segmentation accuracy.

## what is one shot learning
The one-shot learning problem in face recognition involves identifying a person given only one image. Traditional deep learning methods struggle with this due to limited training data. 
to solve this we can use the similarity function
Similarity Function: Train a neural network to output a measure of similarity (or difference) between two images. If the images are of the same person, the function should return a small number; if they are different, a larger number.
Recognition: When a new image is presented, compare it with images in your database using this similarity function. If the similarity score is below a certain threshold (tau), you conclude that it’s the same person; otherwise, it's different.

## siamese networks
By comparing the encodings of two images, you can effectively determine how similar or different they are. 

## triplet loss
The goal is to ensure that the distance between encodings of the anchor and the positive image (same person) is smaller than the distance between the anchor and the negative image (different person) by at least a margin α.
 refer loss function in video
 During training, the network learns to produce encodings such that the distance between encodings for the same person is minimized, while the distance between encodings for different persons is maximized.

to make training effective, it’s important to choose "hard" triplets where the distance between the anchor and positive is close to the distance between the anchor and negative. Randomly chosen triplets might be too easy and not contribute much to learning.

you can use binary classification also here, where difference between encodings is 0 if image is of the same person, and 1 if different persons.

## neural style transfer
 combines the content of one image with the style of another.
 How the CNN can be interpreted
 Layer 1: Detects basic features such as edges and simple textures. The activations in this layer correspond to specific orientations and colors in small patches of the image.

Layer 2: Combines these simple features to detect more complex patterns and shapes. For instance, it might recognize vertical textures or round shapes.

Layer 3 and Beyond: Continues to build on these features to recognize even more complex patterns. By layer 4 and 5, the network begins to detect more abstract representations such as specific object parts (e.g., dog legs) or even entire objects (e.g., dogs, flowers).


Content Loss: Ensures that the content of the generated image resembles the content of the content image. This is typically computed using deeper layers that capture high-level features.
Style Loss: Ensures that the style of the generated image matches the style of the style image. This is computed using the correlations between feature maps at different layers, capturing texture and pattern details.
refer loss functions in video




