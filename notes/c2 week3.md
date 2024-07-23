# Tuning process
  - Tuning hyperparameters is important to get the best out of them
  - Try random values: dont use a grid
  - If computational resources are less, Babysitting model can be used i.e run a single model and change your parameters each day
  - Else, different models can be trained in parallel

---

# Batch normalization
  - Speeds up learning process
  - We normalize A[l] to train W[l+1], b[l+1] faster?
  - Usually applied with mini batches

---

# Softmax Regression
  - Used in multiclass classification
  - In the last layer instead of sigmoid this function is used
