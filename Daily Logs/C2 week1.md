# Improving Deep Neural Networks

## Train / Dev / Test Sets
The model is trained on the training set, refined for the correct algorithm on the dev set and tested on the test set. In the previous era, the ratio was set to 60 : 20 :30. But with the rise of Big Data, the ratio is now almost 99 : 0.4 : 0.6
Make sure that the training and development sets come from the same distribution

## Bias and Variance
1. High bias in model leads to underfitting
2. High Variance leads to overfitting
3. High Bias and High Variance leads to a tightly underfit model which gives high error for training set and high error for dev set 
4. At the Bias-Variance Tradeoff, we find the optimal values for the right classification curve.

Higher Bias can be can be reduced using Bigger Networks, choosing appropriate NN Architecture or introducing more layers
Higher Variance can be can be reduced using Regularisation, Getting more data or a better NN Architecture

## Regularization
1. L1 Regularization : Makes W sparse and thus is useful for compressing the model
2. L2 Regularization : (lambda / 2m) ||w||2F -> also called Frobenius norm
3. Dropout Regularisation: Knock out a percentage of the nodes so that you have a relatively small neural network after every iteration. Appplied only during Train time not test time. At test time we can directly add noise to the data.
4. Data Augmentation :Data augmentation is a technique used to increase the diversity of your training data without actually collecting new data. methods used are : horizontal flipping, rotating, cropping, scaling, etc
5. Early Stopping : It involves monitoring the model's performance on a validation dataset during training and stopping the training process when performance ceases to improve.

## NORMALIZING Input
1. Subtract mean
2. Normalize Variance

**Why?** 
With unnormalised input, gradient descent will yield very wierd values in space. But with normalisation, features are on a similar scale, so the plot is symmetric and it is easy ot optimise

## Vanishing and Exploding gradients
The **vanishing gradient** problem occurs when the gradients of the loss function with respect to the parameters (weights) become very small during backpropagation. This causes the updates to the weights to be insignificant, resulting in very slow learning.
The **exploding gradient** problem occurs when the gradients become very large during backpropagation. This leads to large updates to the weights, which can cause the model to become unstable and fail to converge.

## Gradient Checking 
Gradient checking is a technique used to verify the correctness of the gradients computed during backpropagation in a neural network. It helps ensure that the implementation of the backpropagation algorithm is correct, which is crucial for training accurate models.

It takes all the matrices of Weights and vectors of biases and reshapes them into a single vector theta
Similarly, for db and dw it reshapes to form the vector dtheta of the same dimension
