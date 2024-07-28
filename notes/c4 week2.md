# Some CNN network
  - LeNet-5
      - Identify handwritten digit in `32x32x1` image
      - Published in 1998
  - AlexNet
      - Classify image in 1000 classes
      - Similar to LeNet-5 but bigger
  - VGG-16
      - Modification of AlexNet
      - 138 million params
  - ResNet
      - Skip connections
      - Built out of Residual blocks
      - Because of the vanishing and exploding gradients problems the performance of the network suffers as it goes deeper. Using Residual Network we can go deeper as we             want now.
      - `a[l+2] = g( z[l+2] + a[l] )
	       = g( W[l+2] a[l+1] + b[l+2] + a[l] )`
      - Dimensions of z[l+2] and a[l] have to be the same
  - Inception

---

# Network in network
  - 1x1 convolution
  - Shrink number of channels. Also called feature transformation
