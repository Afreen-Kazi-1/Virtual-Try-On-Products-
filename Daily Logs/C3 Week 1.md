# Introduction to ML Strategy
to improve performance of the model we can implement several ideas like collect more data, diverse data, training algorithms longer with graduent descent, try adam optimizer, try bigger or smaller network, dropout, L2 regularization, change network architecture etc

**But How to chose which idea to be implemented and when?**

## Orthogonalization
This technique is use dto work on each thing individually so as to make sure changes in 1 hyperparamter do not affect the values of other hyperparameters

## Single Number Evaluation Metric
It combines the *Precision* and *Recall* of a model into a single number evaluation metric called F1Score
F1Score is the average of the Precision and the Recall

## Satisfcing and Optimising metrics :
If we have N metrics, we maximise(optimize 1 matrix) and have N-1 Satisficing Metrics

## Distribution of Train/Dev/Test Sets
If data has multiple classes, make sure you shuffle all the data before training / befor dividing it into train and test sets
Size of the test set should be large enough to ensure high confidence in the overall performance of the system

## Comparing to Human Level Performance
Bayes OPtimal Error : Best Possible Error a model can achieve (slightly better than human level error
Human Level Error is often used as a proxy for Bayes Error

## Avoidable Bias
Avoidable bias, also known as reducible or preventable bias, refers to errors in a machine learning model that can be minimized or eliminated through improved data collection, preprocessing, or model training techniques.
It refers to biases you don't need to fix.

