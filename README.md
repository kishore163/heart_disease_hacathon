# heart_disease_Prediction along with a streamlit app

Link TO the notebook: https://colab.research.google.com/drive/18CZgMgMP0GfVX3aouoDLQDHXxXtrCnjM?usp=sharing

## About Dataset
The link to the website containing the dataset is is: https://archive.ics.uci.edu/ml/datasets/Heart+Disease

dataset is taken from UCL website and it contains 14 columns.
They are
1. #3 (age)
2. #4 (sex)
3. #9 (cp)
4. #10 (trestbps)
5. #12 (chol)
6. #16 (fbs)
7. #19 (restecg)
8. #32 (thalach)
9. #38 (exang)
10. #40 (oldpeak)
11. #41 (slope)
12. #44 (ca)
13. #51 (thal)
14. #58 (num) (the predicted attribute)

## 1.Preprocessing the data

The data is analysed primarly to understand more about the data. The null values contained ? symbol and they were treated here. The string values were converted to float values in 2 columns(i.e thal and ca)

## 2.EDA

After primary analysis the data was visulalized using seaborn and matplotlib to understand the correlation between various attributes with each other and also to understand the data in a much better way.

## 3.Splitting the data

The data is splitted into train and test to make sure that we can accurately evalute out model.


## 4.Model building
I have used 4 models to see which one gives the best output and built all 4 models. They are
 1.Logistic regression
 2.KNN
 3.Descision Tree
 4.Random forest 
 
 ## 5. Evaluating the model
 
 Logistic regression was found out to be the best model so I have selected that as my main model and evaluated the score
 
 ## 6.Predicting the output
 
 The model predicts whether a person is suffering from heart disease or not
 
