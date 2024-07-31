## Intersection over Union
Computes size of intersection over size of Union. It is a measure of overlap between bounding boxes. 
The model gives the "correct" bounding box if the IoU is greater than or equal to 0.5

## Non- Max Suppressions (NMS)
To make sure the algo detects one object just once
Conserves bounding boxes with maximum IoU and supresses the non-maximum ones

## Anchor boxes
To identify multiple overlapping boxes

Anchor boxes are a crucial concept in modern object detection algorithms like Faster R-CNN, SSD (Single Shot MultiBox Detector), and YOLO (You Only Look Once). They help in handling objects of different scales and aspect ratios in images. 

they are :
Predefined bounding boxes of different sizes and aspect ratios.
Placed uniformly across the image, serving as references or templates for predicting object bounding boxes.

## YOLO : Putting it Together
YOLO : You Only Look Once

YOLO (You Only Look Once) is a real-time object detection system that reframes object detection as a single regression problem, straight from image pixels to bounding box coordinates and class probabilities. Unlike traditional methods that apply the model to an image at multiple locations and scales, YOLO applies a single neural network to the full image.

in YOLO :
- For each grid call , get predicted bounf=ding boxes
- Get rid of low probability predictions
- For each class, use non-max supression to generate final prediction

## Region Proposal:
R-CNN : Propose regions, Classify one region at a time, output label and bounding box.
