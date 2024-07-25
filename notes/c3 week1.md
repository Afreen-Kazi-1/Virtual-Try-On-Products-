# Improving Model performance
  - Collect more data
  - Collect more diverse training set
  - Try regularization
  - Try dropout
  - Change network architecture
  - Train algorithm longer with gradient descent
  - Try different optimizers
  - If doing well on your metric + dev/test set doesn't correspond to doing well in your application, change your metric and/or dev/test set.
---

# Orthogonalization
  - Knowing which hyperparameter to tune to achieve a certain effect

---

# Single number evaluation metric
  - Better and faster to set a single number evaluation metric for the project before starting
  - Combines precision and recall in a single value.

---

# Satisfying and optimizing metric 
  - We choose a single metric to optimize and other metrics satisfy

---

# Human level performance
  - Bayes optimal error cannot be suprassed
  - So as long as Machine learning is worse than humans, you can:
      - Get labeled data from humans.
      - Gain insight from manual error analysis: why did a person get it right?
      - Better analysis of bias/variance.
  - Human error is a proxy for Bayes optimal error
  - You can't do better than Bayes error unless you are overfitting
