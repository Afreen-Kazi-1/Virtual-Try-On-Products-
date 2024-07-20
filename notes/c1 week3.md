# Neural Networks
  - Each network has 3 layers: input layer, hidden layer and output layer
  - The input layer does not have any activation function associated with it
  - Hidden layer is not visible in the training set

--- 

# Activation functions
  - Passes an output signal to the next layer
  - Without activation function the neural network would be having a linear relationship which is not efficient for learning
  - There are different activation functions such as sigmoid, tanh, ReLU, Leaky ReLU, etc.
  - Sigmoid and tanh functions have the gradient descent problem.
  - ReLU is the most used activation function
  - Linear activation functions are rarely used.

--- 

# Random Initialization
  - Initialising all weights to 0 will make the neural network symmetric i.e each node will be computing the same function
  - To solve this problem W matrix is initialized randomly 
