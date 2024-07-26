# Error analysis

Analyse where maximum error comes from and work on it first.

## Problem with Incorrectly Labelled Data
Calculating Fraction of Mislabelled Data gives an idea for prioritization. 

Incorrectly Labelled Data can be corrected by :
1. Applying same process to dev and test set to make sure they continue to come from the same distribution
2. Consider analysing examples that algo got right as well as the ones it got wrong
3. Train and Dev/Test sets may come from slightly different distributions

## Build First System Quickly, then iterate 
then we can use bias-variance analysis and error analysis to prioritize the next steps

## Training and Testing on Different distributions
It is a common challenge in machine learning where the training data and testing data come from different distributions. This discrepancy can significantly impact model performance because the model learns patterns specific to the training data that may not generalize well to the test data.

so we can:
1. Shuffle Train and Dev set after recombining them
2. Take some test data into training set and keep the dev and test sets from completely test data.
      
   
