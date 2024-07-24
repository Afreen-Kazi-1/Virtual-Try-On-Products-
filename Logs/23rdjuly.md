# 23rd july logs

## Learnt about regularization
Dropout Regularization
Why it can help reduce overfitting 
What are the different intuitions we can have for that
Other types of regularization like early stopping
Just mention of orthogonalization


## Learnt about normalization
it is used to scale the different features we have
we subtract the mean from all the x's  (normalize mean) and also normalize variance
Learnt what is vanishing and exploding gradients problem
These can be solved by normalization
Learnt how different activation functions have different kinds of normalization variances like relu has 2/n superscript [l-1]

## learnt about how two sided gradient checking is more accurate than one sided

## learnt about grad checking
calculated diff between dtheta and dtheta approx
preferably used while debugging
doesnt work well with dropouts

## mini batch gradient descent
divide the data into mini batches
gradient descent will take place for all these batches all together
If you have a large dataset, this is mostly used
Beacuse one single iteration of backprop on the dataset will be too long

If batch size is m then batch gradient descent
If batch size is 1 then schocastic gradient descent
 Batch size 1 will be very noisy gradient descent, mostly never reached to the minimal value of cost function

 Batch size is mostly between 64 to 512, usually prefer exponent of 2

## exponentially weighted averages
Vt=beta times (previous data)+(1-beta) times current data
Vt basically gives us average over 1/1-beta days
higher the val of beta, smoother the curve, lower the value, average is taken over lesser time so noisier curve\

bias correction for inital values of data
divide vt by 1-beta raise to t

## gradient descent with momentum
reduces vertical oscillations of the gradient descent path, and slows down horizontal speed of descent

## RMSprop
same formula of weighted average, you just square dw(element wise sum of squares)
and then while updating dw and db during gradient descent you divide dw and db by root of sdw, sdb
this is also used to reduce vertical oscillations

## adam optimization algorithm
First write vdw, vdb, sdw, sdb equations using exponentially weighted averages and rmsprob method
then find their corrected versions using bias correction
Then while updating dw and db during gradient descent, use vdw(corrected)/root of sdw + epsilon

## learning rate decay
when using mini batch, the descent is going to be noisy, so it wont converge to a proper minima point on the cost function
so what we can do is when it starts reaching close to the minima, we reduce the learning rate so that the descent is sharper and we get the minima
refer formulae

## hyperparameters
Choose important ones
Random selection of values, can use grid method
coarse to fine approach

Choosing the right scale for hyperparameters
How to select beta

## normalization
what is batch normalization and advantages, how it works

## softmax classfier
softmax regression
how softmax works




