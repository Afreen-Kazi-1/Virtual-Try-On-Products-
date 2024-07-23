# Optimization Algorithms

## Mini Batch Gradient Descent
Splits the training set into mini batches so that we can take quicker steps without waiting to process the whole data set
With mini-batch gradient dexcent is more noisy than the whole batch

if minibatch size = size of training set -> batxh gradient descent
if minibatch size = 1 -> Stochastic gradient Descent 

optimally, keep batch size in powers of 2 (64, 128, 256, 512, 1024) -> so that it is easier for the memory to process

## Exponentially weighted averages (Moving Averages) and Bias Correction
A moving average is a technique to smooth out short-term fluctuations and highlight longer-term trends or cycles
Bias correction is used to adjust the moving averages to account for the initialization bias. When starting the moving average calculation, the early values are biased towards zero because the averages are based on fewer data points. Bias correction helps to mitigate this effect.

## Gradient Descent with Momentum
Gradient Descent with Momentum is an optimization technique that helps accelerate the convergence of the gradient descent algorithm, especially in scenarios where the cost surface is shallow and has elongated valleys. The main idea behind momentum is to accumulate the past gradients in the direction of persistent reduction in the cost function, thereby dampening oscillations and speeding up convergence.

##RMS Prop
aim : Slow learning vertically and fast learning horizontally
so reduce b and increase w

## Adam Optimization: Adaptive Moment Estimation 
It is an optimization algorithm that combines the benefits of two other popular methods: Momentum and RMSProp. 
Hyperparameters used : 
1. ALpha : Learning rate. Need to be tuned
2. Beta 1 :  the decay rate for the first moment estimate (commonly set to 0.9).
3. Beta 2 : it is the decay rate for the second moment estimate (commonly set to 0.999)
4. Epsilon :  a small constant to prevent division by zero (commonly set to 10 ^ -8 )

## Learning Rate Decay
Learning rate decay is a technique used to gradually decrease the learning rate during the training process. This can help improve the performance and convergence of the model by allowing for larger updates in the beginning (to quickly converge to a good region) and smaller updates towards the end (to fine-tune the weights).

Types of  Learning Rate Decay :
1. Step Decay: The learning rate is reduced by a factor at specific intervals (epochs).
2. Exponential Decay: The learning rate decreases exponentially over time.
3.  1/t Decay: The learning rate decreases proportionally to the inverse of the epoch number.
