Update : 21st August
## Issue 1 :  
After 1st epoch, number of Tensor inputs changes from 3 to 1.
Reason 1 : 
Probably, 1st layer directly outputs the image, which is fed again leading to a single input. 
Steps taken :
Tried checking what happens with a single epoch. Issue still persists

## Issue 2 :
Assumed issue with VSC compiler. 
Reason : Large dataset
Steps : Switched to Kaggle. But did not verify that the dataset fed as a zip got saved as doc file. 

Will try resolving tomorrow
