# Deep Neural Networks

Def : Deep neural Networks have multiple hidden layers between the input layer and the output layer
here, the feature vector is also represented as a[0] for 1 training example and A[0] for the whole training set

## Vectorised equations for the whole training set :
Z[l] = W[l] A[l-1] + b[l]
output = A[l] = g[l[(z[l]) where g[l] is an activation function

## Why do deep neural networks learn well?
1. Deeper the layers, more complex pattern it can learn
2. Scalability

# Circuit Theory :
There are functions that can be computed with a "small" L-layer DNN that shallowewr netwroks require exponentially more hidden units to compare

#Forward and Backward Functions
[![Equations](https://drive.google.com/file/d/1OE1W88DLU1uRWzPp61XFATB3jfX_-Htj/view?usp=sharing)]

# Parameters and Hyperparameters
parameters include weights and biases of individual layers
Hyperparameters are those that can control the paramters and mpdify them. They include Learning rate (alpha), number of iterations, no. of hidden layers, hidden units, choice of activation function etc.
