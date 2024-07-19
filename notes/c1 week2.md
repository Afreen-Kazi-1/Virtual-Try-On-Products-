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

--- 

# Vectorization
  - Optimizes the code to run faster by removing for loops.
  - numpy uses it by default
  - GPU can process vectorization faster

---

# Broadcasting  
  - Data is converted into higher data type with which some operation is to be performed.
  - If matrix with dimension (m,n) is added with matrix of dimension (1,n), the seconed matrix is broadcasted to the size of (m,n)
