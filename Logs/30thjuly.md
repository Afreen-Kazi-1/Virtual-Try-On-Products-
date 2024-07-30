## LE-NET 5
used for tasks like identifying numbers (handwritten)
typical CNN structure, one or more conv layer, followed by a pooling layer (average pooling)...then softmax which will actually predict the value of the number
about 60k parameters as compared to the 10 million we have today


 ## AlexNet
AlexNet takes in images of size 227x227x3. Though the original paper mentions 224x224x3, the dimensions work out more accurately with 227x227x3.
First Convolutional Layer:

Filters: 96 filters of size 11x11
Stride: 4
Output Volume: 55x55x96 (due to the large stride, the dimensions shrink)
First Max Pooling Layer:

Filter Size: 3x3
Stride: 2
Output Volume: 27x27x96
Second Convolutional Layer:

Filters: 256 filters of size 5x5 (same padding)
Output Volume: 27x27x256
Second Max Pooling Layer:

Filter Size: 3x3
Stride: 2
Output Volume: 13x13x256
Third Convolutional Layer:

Filters: 384 filters of size 3x3 (same padding)
Output Volume: 13x13x384
Fourth Convolutional Layer:

Filters: 384 filters of size 3x3 (same padding)
Output Volume: 13x13x384
Fifth Convolutional Layer:

Filters: 256 filters of size 3x3 (same padding)
Output Volume: 13x13x256
Third Max Pooling Layer:

Filter Size: 3x3
Stride: 2
Output Volume: 6x6x256
Fully Connected Layers:

The final volume (6x6x256) is flattened into a vector of 9216 nodes.
This is followed by a few fully connected layers.
The network ends with a softmax layer for classification into one of 1000 possible categories.

AlexNet has about 60 million parameters compared to LeNet's 60,000.
AlexNet uses the ReLU activation function, which helps in faster training compared to the sigmoid activation used in LeNet.

## VGG 16
The main idea behind VGG-16 is to use small 3x3 filters consistently and maintain the same padding and stride of one throughout the network. Max pooling layers with 2x2 filters and a stride of two are used to reduce the spatial dimensions.
Input Layer:

Takes in images of size 224x224x3.
First Convolutional Block:

Two Conv Layers: Each with 64 filters of size 3x3, same padding, stride 1.
Output Volume: 224x224x64.
Max Pooling: Reduces the volume to 112x112x64.
Second Convolutional Block:

Two Conv Layers: Each with 128 filters of size 3x3, same padding, stride 1.
Output Volume: 112x112x128.
Max Pooling: Reduces the volume to 56x56x128.
Third Convolutional Block:

Three Conv Layers: Each with 256 filters of size 3x3, same padding, stride 1.
Output Volume: 56x56x256.
Max Pooling: Reduces the volume to 28x28x256.
Fourth Convolutional Block:

Three Conv Layers: Each with 512 filters of size 3x3, same padding, stride 1.
Output Volume: 28x28x512.
Max Pooling: Reduces the volume to 14x14x512.
Fifth Convolutional Block:

Three Conv Layers: Each with 512 filters of size 3x3, same padding, stride 1.
Output Volume: 14x14x512.
Max Pooling: Reduces the volume to 7x7x512.
Fully Connected Layers


VGG-16 has about 138 million parameters, making it a large network even by modern standards.


## resnets
used to train very deep neural nets easily
so instead of following the usual path, resnet adds lets say the activations of the lth layer to the linear function of the l+2 layer before finally applying the relu function to the l+2 layer.

this is called as a skip connection or a residual block.
in a deep neural network, multiple residual blocks are stacked together.

## one on one convolutions
Reducing Channels:
Consider an input volume of size 
28×28×192.
To reduce the number of channels to, say, 32, you can apply 32 filters of size 
1×1×192.

## inception module
The Inception module applies 1x1, 3x3, and 5x5 convolutions as well as a pooling layer (typically max pooling) to the input volume.
Each operation produces an output volume of the same spatial dimensions (height and width) but potentially different depths.
Concatenation:

The outputs of these different convolutions and pooling operations are concatenated along the depth dimension, resulting in a new, deeper volume.
