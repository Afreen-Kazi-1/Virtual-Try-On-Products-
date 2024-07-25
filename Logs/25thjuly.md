# Orthogonalization
## Orthogonalization basically means that: we know there are four stages of building our neural network
1. Training the NN
2. Development set
3. Test set
4. Whether it performs good in the real world too

So suppose there is a problem in either one of them. Then it will be good if we have a specific set of controls that will help us solve that particular problem.
Let us consider that we have a problem in training, then perhaps we can get more data, or use another optimization algo or something like that.
The basic idea is just that there should be different controls (like different knobs to control a tv set) for different issues.
Like now, early stopping doesnt have that much good orthogonalization because it affects two things, training as well as overfitting


# Precision and recall
## Precision
Of all the images classified as cats by the classifier how many are actually cats
## Recall
Of all the cat images in the data,how many did the classifier actually recognize
## F1 Score 
Is a single real number evaluation metric that tells us about how good a model is...it is basically the harmonic mean of precision and recall


# Optimizing and satisficing metrics
When we have multiple factors that we care about, we can set one as optimizing and the other as satisficing
For exp for our NN model consider two factors, accuracy and computing time. Here we can set the time as always less tha 100 ms and we can maximize our accuracy. Here time is satisficing, ie as long as it is less than 100 ms you are good to go, and accuracy is the optimizing, ie you have to maximize that.

# Training and dev/test set distributions
Trditionally it was 70 30 or 60 20 20 because data was less
now its 99 percent trauning and 1 percent each for decv and test

Dev set and evaluation metric is like defining a target for hitting and then that i s a separate task to optimize hwo you will hit that.

It is possible that during the course of training, you work with some evaluation metric, say error. Now there are two algorithms a and b and b has higher error as proven by the dev set. so a is working well on the dev set. but in real life, the dataset changes a bit and then b starts workinbg better. in this case you will have to change eithe ryour dev/test set because it made  you make inaccurate conclusions or also change your evaluation metric.

![orthogonalization in this]( C:\Users\Mahi\OneDrive\Pictures\Screenshots\Screenshot 2024-07-25 164720.png)

# Bayes error
it is the minimum error that you can reach, it is practically less than human error too.
Avoidable bias is the diff in error of the training set and human error(which is approx equal to bayes error)
And variance is equal to the diff between dev and training error

if avoidable bias is very high, focus on reducing that
if variance is very high and avoidable bias is low, focus on reducing variance

## To reduce avoidable bias we can do:
Train a bigger network, train the network longer or use better optimization methods, change the NN architecture, hyperparameter tuning
## To reduce variance
Regularization, get more training data, hyperparameter tuning

## Error analysis
You manually take a look at data which has been classified incorrectly and find classes within that mislabelled data, like suppose for cat classifier, there can be many error categories like it mis classified big cats like tigers, or images were blurry etc etc
You find wich category contributes the most to the error and can then proceed to work on that
 ## mislabelled data
 mislabelled data in the training set doesnt matter, beacause the training set is huge
you can correct mislabelled data in the dev set if it reduces your error significantly

 # Type of data for train and test/dev sets
 Suppose if you have a cat classifier app, you have only 10k actual cat pictures uploaded by users, and 1 million other pictures taken from the internet. Shuffling and distributinh them isnt a good idea. What you can do is put half of user photos into the training set and divide the rest into dev and test sets. 

 ## Train-dev set
 you take out a section from the train set, but dont train the model on it.
 You calculate the bias, variance, data mismatch, and then decide what you have to do

 ## Solving the data mismatch problem
 Using artificial data synthesis you can make the training data much more similar to the test/dev data.

 ## Transfer learning
  technique where a pre-trained model, developed for a specific task, is adapted for a different but related task.
  It is useful when:Task A and B have the same input X.(audio, or video)
  And because data for Task B is more valuable for Task B, usually you just need a lot more data for Task A because , each example from Task A is just less valuable for Task B than each example for Task B
  low level features from Task A could be helpful for learning Task B

## Multi task learning
   In multi-task learning, a single neural network is trained to perform multiple tasks simultaneously, such as detecting pedestrians, cars, stop signs, and traffic lights in autonomous driving.
   More common in scenarios where multiple related tasks need to be solved together, such as object detection in computer vision. Generally used less frequently than transfer learning due to the complexity of finding multiple related tasks.


## End to end learning
The model learns directly from the data without needing to follow intermmediate steps.
End-to-end learning requires large amounts of labeled data to effectively learn the direct mapping from 
x to y. Insufficient data can lead to poor performance. you need a big enough NN as well.

