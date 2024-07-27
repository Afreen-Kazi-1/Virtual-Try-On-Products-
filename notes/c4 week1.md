# Strided convolution
  - Used in CNNs
  - Number of pixels to jump when convolving a filter
  - if a matrix `nxn` is convolved with `fxf` filter/kernel and padding `p` and stride `s` it give us `(n+2p-f)/s + 1,(n+2p-f)/s + 1` matrix.

---

# Convolutions over volume
  - Convolve an image of height, width, # of channels with a filter of a height, width, same # of channels.

---

# CNN
  - First convolve some filters to the given image then add the bias and then apply the activation function
  - Input size decreases over the layers but the filters increase
---

# Pooling layers
  - Reduces the size of input and speeds up the computation
  - No parameters to learn
  - Max pooling and average pooling
  - Max pooling is used more often

---

# Advantages
   - Parameter sharing
        - A feature detector that's useful in one part of the image is probably useful in another part of the image.
   - sparsity of connections
        - In each layer, each output value depends only on a small number of inputs which makes it translation invariance.
