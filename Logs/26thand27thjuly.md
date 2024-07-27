## Convolution
convolution is a mathematical operation on two functions that produces a third function
CNNS Used in edge detection, face recognition tasks etc.

Each element of the filter is multiplied by the corresponding element of the image, and the results are summed to produce a single value.
This value is placed in the corresponding position in the output feature map.
The filter is then shifted one pixel to the right and the process is repeated until the entire image has been processed.

## Vertical edge detection filters, horizontal edge detection filters, sobel filters

## Learning Filters with Backpropagation:
Instead of handpicking filter values, the parameters of a filter can be learned using backpropagation.

## Padding
Padding adds a border of extra pixels around the image, usually with zeros, to maintain the original image size after convolution.

## Striding
Stride refers to the number of pixels by which we move the filter across the image.
A stride of 1 means moving the filter one pixel at a time, whereas a stride of 2 means moving it two pixels at a time.

## Convolutions over volume
To convolve with a 3D image, we use a 3D filter. For example, a 
3×3×3 filter, where the last dimension must match the number of channels in the input image.
The filter also has a height, width, and number of channels.

## Pooling
Max pooling selects the maximum value from each patch of the feature map covered by the filter.
Average pooling computes the average value from each patch of the feature map covered by the filter.

## Advantages of CNNS
Parameter Sharing
Parameter sharing gives the idea that a feature detector useful in one part of the image is likely useful in another part of the image
Sparsity of Connections
Convolutional layers have sparse connections, meaning each output neuron is connected to only a small, localized region of the input

