# Train/Test/Dev sets
  - Not possible to get hyperparameters right in the first try.
  - Training data has to be the largest
  - Dev and test sets should be from the same distribution

---

# Bias and Variance
  - Model - underfitting - high bias
  - Model - overfitting - high variance
  - If model has high bias:
      1. Make Neural network larger
      2. Use different optimizer
  - If model has high variance:
      1. Gather more data
      2. Use regularization
   
---

# Regularization
  - Reduces overfitting

## Dropout Regularization
  - Eliminates neurons in a layer based on probability
  - Not used during testing else it will add noise
  - Input layer must have dropout probability close to 0 as too many features should not be eliminated
  - Many researchers use dropout with CV

## Data augmentation
  - Flip the image by random angles
  - Obtaining new data is better than this technique

---

# Normalization
  - Speeds up the training process
  - The cost function will be consistent and easier to optimize

---

# Vanishing/Exploding gradient
  - When derivatives become very small or very big
  - Increases computation and reduces learning efficiency
  - Initialization of weights correctly is important to avoid this
    
---

# Gradient checking
  - Checks whether implementation of back propagation is correct
  - Used only for debugging
  - Doesn't work alongside dropout
