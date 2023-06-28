# R&R-Machine Learning - Diabetes Prediction

## Project/Goals
Analyzing the contributing factors to diabetes, and predicting if a person is likely to have diabetes based on the parameters available.
The dataset used is the [Pima Indians Diabetes Database from Kaggle](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database), where you can see all the columns and what they represent. The dataset contains information about 768 patients and their corresponding nine unique attributes.

## Process
Explored the data to understand the different component of the dataset
![image](https://github.com/Jagunmolu-dev/LIGHTHOUSELABS/assets/67484584/a17a0513-7375-4788-b0fe-2f1639c3ecae)

EXPLORATORY DATA ANALYSIS
The dataset used has a shape of (768, 9): To properly predict if a person has diabetes or not we would need more data to split into the test and train set, but for this research, we will make do with the available data.


# Step 2: 
> Investigating the Relationship between Age and BMI
![image](https://github.com/Jagunmolu-dev/LIGHTHOUSELABS/assets/67484584/26ae5de1-de9f-48fc-af14-9a92781f4a88)
### The scatter plot shows the relationship between the Age and BMI columns of the diabetes dataset. Each point represents a patient in the dataset. The color of each point represents whether the patient has diabetes (yellow) or not (purple). The plot shows that there is no clear relationship between Age and BMI, and that there are both diabetic and non-diabetic patients across all ages and BMIs.

> Analyzing the distribution of the different contributing factors
![image](https://github.com/Jagunmolu-dev/LIGHTHOUSELABS/assets/67484584/1d0b6263-4452-4567-bee0-6f379655e748)
### The histograms show the distribution of values for each column.

> Analyzing each feature to see how they are correlated.
![image](https://github.com/Jagunmolu-dev/LIGHTHOUSELABS/assets/67484584/509bd1fd-4963-4db6-ab3c-bbe977a728e1)
### The heatmap shows the correlation between each pair of columns as colors. The colors range from blue (negative correlation) to red (positive correlation) and In the heatmap, values close to 1 indicate a strong positive correlation between the two variables.

> MACHINE LEARNING
### I used different ML algorithms on the dataset to predict diabetes. I found that the model with Logistic Regression (LR) and Support Vector Machine (SVM) works well on diabetes prediction. Using the sklearn.metric and importing the accuracy score, the Accuracy Score of the training data: 0.7866449511400652 which is approximately 79%, and the Accuracy Score of the testing data: 0.7727272727272727 which is approximately 77%.
The accuracy of the data might be lower due to the small amount of data

## Results
##Testing the data to validate our model and it predicted correctly if a person has diabetes or not.
![image](https://github.com/Jagunmolu-dev/LIGHTHOUSELABS/assets/67484584/c27403df-405c-4f40-914a-1c3f7c541524)

## CONCLUSION
Early detection of diabetes is one of the significant challenges in the healthcare industry. In our research, we designed a system, which can predict diabetes with high accuracy. 
All models provided an accuracy greater than 70%. LR and SVM provided approximately 77%–78% accuracy for both train/test split.

It is important to note that machine learning models are not perfect and may not always provide accurate predictions. It is also important to ensure that the data used to train the model is representative of the population being studied.


## Challenges 
The amount of data available is not sufficient to make predictions with a high accuracy.


