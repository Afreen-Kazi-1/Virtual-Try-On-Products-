# Binary Classification
  - The output is yes or no. For example, predicting whether the input image contains a cat or not.
    
---

# Logistic Regression
  - It is used to classify 2 classes.
  - Sigmoid function is used.

## Loss and cost functions
  - Loss function calculates the error for a single training data
  - Cost function is the average of loss function over the entire training data

## Gradient descent
  - It is used to find w and b which minimizes J(w, b) i.e the cost function
  - The cost function we use is convex hence gradient descent can be applied to it.
  - We initialise w and b with some values and move towards the global minima of the function
