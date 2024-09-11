## inception networks
key ideas:
Using multiple filter sizes (1x1, 3x3, 5x5) and pooling in parallel.
Concatenating the outputs along the depth dimension.
Reducing computational cost by using 1x1 convolutions as bottleneck layers.
An Inception network is composed of multiple Inception modules stacked together. It typically includes additional layers for input preprocessing, output classification etc

## mobilenets
used in devices with low computational powers, like mobiles
Depthwise Separable Convolution: Significantly reduces the number of multiplications

watch video for details, difficult to note down here

MobileNet v1 employs a stack of layers, each consisting of a depthwise convolution followed by a pointwise convolution. This structure is repeated 13 times to transform the raw input image into a final classification prediction. 
 After these 13 layers, the network includes:

A pooling layer
A fully connected layer
A softmax layer for classification
MobileNet v2 Architecture
MobileNet v2 introduces two key enhancements to improve the performance of the network while maintaining computational efficiency:

Residual Connections:

Similar to ResNet, these connections allow gradients to propagate more efficiently during backpropagation by directly passing the input from one layer to the next.
Expansion and Bottleneck Blocks:

Each block consists of:
An expansion layer: Applies a 1x1 convolution to increase the number of channels (typically by a factor of 6).
A depthwise convolution: Maintains the spatial dimensions while performing convolution on each channel separately.
A projection layer (or pointwise convolution): Reduces the number of channels back to the desired output size.

## efficient net
you can adjust the resolution of the image, width of the filters, or depth of the NN.



