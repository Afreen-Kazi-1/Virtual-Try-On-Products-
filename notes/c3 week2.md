# Error analysis
  - Manually checking the mistakes of your algorithm

---

# Training and testing on different distributions 
  - Option 1: Shuffle all data and randomly extract training and test/dev sets. This is not recommended though
  - Option 2: Add some examples of dev/test set to the training set

---

# Data mismatch
  - `data mismatch = dev error - train-dev error`
    - If difference is much bigger then train-dev error its Data mismatch problem.
  - Make training data more similar or collect more data similar to dev/test set
  - Artificial data synthesis can be used

---

# End to end deep learning
  - Combines multiple stages into a single stage
  - We need a huge dataset
  - Applying end-to-end deep learning:
    - Key question: Do you have sufficient data to learn a function of the complexity needed to map x to y?
    - Use ML/DL to learn some individual components.
    - When applying supervised learning you should carefully choose what types of X to Y mappings you want to learn depending on what task you can get data for.
