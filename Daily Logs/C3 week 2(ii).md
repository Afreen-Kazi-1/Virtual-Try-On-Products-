## Training-Dev Set :
It comes from the same distribution as Training set, but not used for training the model.

1. Avoidable Bias : The difference between human-level proxy for Bayes error and Training error. Can be removed using better optimisation or bigger model
2. Variance : The difference between Training-Dev set error and training error. Can be removed using more data, regularization or bigger networks
3. Data Mismatch Problem : Difference in dev set error and training-dev set error.
4. Degree of overfitting to dev set : Difference between test set error and dev set error. (Although test set is not trained upon

## Data Mismatch :
Happens because Train and Dev/Test sets come from different distributions

## Addressing Data Mismatch
1. Carry out manual error analysis to try to understand difference between train and dec/test sets 
2. Make training data more similar or collect more data similar to dev/test sets using artificial data synthesis

## Transfer Learning
Models trying out one purpose say image recognition can be used to train or applied for other purposes like radiology diagnosis 

Make sense when there is a lot of data for the problem to be transferring from and less data for the problem we are transferring to

works well when :
1. Tasks A and B have same input X
2. You have a lot more Data for A than for B
3. Low level features from A can be helpful for learning in B

## Multitask Learning
Here one image has multiple labels

# End to end learning
Some Data processing/learning system requires multiple processing steps which can be replaced and rearranged using a single neural network with end-to-end learning.
