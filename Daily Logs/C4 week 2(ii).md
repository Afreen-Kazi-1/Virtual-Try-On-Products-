# Network In Network 
1x1 Convolutional Networks -> Not Much Effective  with 2D matrices with single channels

With a multiple channel 1x1 filter, we can reduce the number of feature channels from the input. 

## Inception Network 

The Inception network, also known as GoogLeNet, is a deep convolutional neural network architecture that introduces the concept of Inception modules. These modules allow the network to perform multiple convolutional operations with different filter sizes (1x1, 3x3, 5x5) and pooling operations (3x3 max pooling) in parallel, concatenating their outputs. This approach allows the network to capture multi-scale features while keeping computational efficiency.

 Problem : Computational Cost (can be reduced using 1x1 conv nets

We can also use open Source from github from Deep Learning guys

## Transfer Learning : 
here we use other models as initialisation for your model. 
very valuable if other models have very large data and our model has comparatively smaller data
It freezes some of the layers of the available model and retrains the rest for the current model. So it uses pretrained weights to save time

## data Augmentation
Increases the data set to improve efficiency
Uses methods like :
- Random Cropping
- Mirror
- colour Shifting

## State of Computer Vision
To do well on benchmarks : 
- ensemble : Train several netwroks independently and avearge their outputs
- Multicrop at test time : Run Classifier on multiple versions of test images
- use opensource and implementations
