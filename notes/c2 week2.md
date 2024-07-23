# Mini batch gradient descent
  - Split the dataset into smaller datasets and run gradient descent on them
  - Works much faster in large datasets
  - Mini batch size is a hyperparameter

---

# Exponentially Weighted average
  - Formula: `V(t) = beta * v(t-1) + (1-beta) * theta(t)`
  - Becuase `V(0) = 0` the weighted average is shifted. To solve this bias is introduced
  - New Formula: `v(t) = (beta * v(t-1) + (1-beta) * theta(t)) / (1 - beta^t)`

---

# Gradient descent with momentum
  - Faster than standard gradient descent
  - Calculate exponentially weighted average for the weights and update them accordingly
  - In practice, people don't bother adding bias correction

---

# RMSprop
  - Root mean square prop
  - Cost function will move slower in vertical direction and faster in horizontal direction

---

# Adam optimization algorithm
  - Adaptive moment estimation
  - Puts RMSprop and momentum together
    
---

# Learning rate decay
  - Reducing the learning rate
  - Lesser priority
