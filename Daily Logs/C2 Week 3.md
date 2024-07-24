# Hyperparamter Tuning

## Tuning Process
For finding optimal hyperparmaters, use random search instead of grid search

Hyperparameters in decreasing order of importance
1. Alpha
2. beta, minibatch size, hidden units
3. no.of hidden layers, learning rate decay

Coarse to fine scheme 
With random search if we discover the set of hyperparameters in a particular space are giving better input, we sample more finely in that particular space to get better Hyperparamters

## Pandas v/s Caviar 
Cross - Fertilization : Techniques developed and tested in one field cam also be applied to other fields

Pandas : Babysit a single Model because of lack of high computational facilities. This is very slow
Caviar : Training multiple models in parallel if there is availibility  of high computational facilities.It is relatively faster 

## Batch Normalization
Batch normalization (BatchNorm) is a process applied during training to normalize the inputs of each layer so that they have a mean of zero and a standard deviation of one. This normalization is done across the mini-batch dimension.
This also works with momentum, RMSProp and Adam OPtimization

## Why BatchNorm Works?
By normalizing the inputs to each layer, batch normalization helps to mitigate the problem of internal covariate shift, where the distribution of inputs to a layer changes during training. This stabilization can lead to faster convergence. 

At test time, batchNorm calculates mean and variance using exponentially weighted averages (accorss mini batches)

BatchNorm also has a slght regualrization effect

## Softmax Regression
Softmax regression, also known as multinomial logistic regression, is a generalization of logistic regression that is used when there are more than two classes to predict. It is commonly used for classification problems where the target variable is categorical with more than two classes.

Softmax activation function (z(i)) = exp(z(i)) / sum(exp(z(j))[j = 1 to C])

The softmax function ensures that:
1.The output values are between 0 and 1.
2. The sum of the output values is 1.

The cost function used in softmax regression is the cross-entropy loss, which measures the performance of a classification model whose output is a probability value between 0 and 1.

## Problem of Local Optima
The problem of local optima refers to the challenge in optimization algorithms where the algorithm gets stuck in a local optimum, which is a solution that is better than its neighboring solutions but not necessarily the best overall solution (global optimum). 
The point where derivative is zero is called the **saddle point**
The region of the set of points where the derivative tends towards zero for a long time is called a *plateu* 
