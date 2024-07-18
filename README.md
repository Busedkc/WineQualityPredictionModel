# Wine Quality Prediction Model Project

The object of this project is to predict the quality of red wine using machine learning. 
The dataset used for this project is the “winequality-red.csv” (from kaggle) dataset which consists of 1599 instances and 12 attributes. 
The attributes include fixed acidicity, volatile acidity, critic acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, 
density, pH, sulphates, alcohol and quality. The quality attribute is the target variable which is the quality rating of the wine ranging from 0 to 10.

## Data Processing

The first step of any machine learning project is to preprocess the data. In this project, we have loaded the dataset using pandas and created 
two variables - predictor (X) and target (y). We have dropped the quality column from the predictor variable and created a new target variable 
where the quality rating is classified as 1 if it is greater than or equal to 7 and 0 otherwise. This is done to convert the problem into a binary 
classification problem. We have also split the data into training and testing sets using the train_test_split function from scikit-learn.

## Model Training

We have used the Random Forest Classifier algorithm to train the model. The Random Forest Classifier is an ensemble learning method that uses 
decision trees to make predictions. It works by constructing multiple decision trees during training and outputting the class that is the mode 
of the classes (classification) or mean prediction (regression) of the individual trees. We have trained the model using the training data and 
calculated the accuracy of the model on the test data.

## Web Application

We have also created a web application using Streamlit which allows the user to input the features of the wine and get the predicted quality 
rating. The user inputs the features separated by commas in a text box, and the web application outputs whether the wine is of good or bad quality 
based on the predicted quality rating.

## Conclusion

In this project, we have successfully predicted the quality of red wine using machine learning. We have used the Random Forest Classifier algorithm 
and achieved an accuracy of 70% on the test data. We have also created a web application using Streamlit which allows the user to input the features 
of the wine and get the predicted quality rating. This project can be extended by using other machine learning

## About Data

The data provided appears to be a tabular dataset with 12 columns and multiple rows, where each row represents a sample of wine and each column represents 
a different features of that wine. The features are descibed below:

- Fixed acidity: the amount of fixed acids in the wine (g/dm^3)

- Volatile acidity: the amount of volatile acids in the wine (g/dm^3)

- Citric acid: the amount of critic acid in the wine(g/dm^3)

- Residual sugar: the amount of residual sugar in the wine (g/dm^3)

- Chlorides: the amount of chlorides in the wine (g/dm^3)

- Free sulfur dioxide: the amount of free sulfur dioxide in the wine (mg/dm^3)

- Total sulfur dioxide: the amount of total sulfur dioxide in the wine (mg/dm^3)

- Density: the density of the wine (g/cm^3)

- pH: the pH level of the wine

- Sulphates: the amount of sulphates in the wine (g/dm^3)

- Alcohol: the alcohol content of the wine (% vol)

- Quality: a rating the quality of the wine (scored between 0 and 10)

## About Code

Here, we are reading the wine dataset from a CSV file using Pandas and storing it in a Pandas DataFrame called wine. 

We’re creating the predictor variable X by dropping the quality column from the wine_df DataFrame. We’re creating the target variable 
y by applying a lambda function to the quality column, which sets the value of 1 for quality score of 7 or higher and 0 for quality scores below 7.

We’re splitting the dataset into training and testing sets using the train_test split() function from Scikit-learn. The training set contains 80% 
of the data, and the testing set contains 20% of the data. The random_state parameter sets the seed value for the random number generator to ensure 
that we get the same results every time we run the code.

We’re initializing a Random Forest Classifier model and fitting it to the training the data using the fit() method. 

We’re using the trained model to predict the wine quality for the testing data and calculating the accuracy of the model on the testing data using 
the accuracy score() function from Scikit-learn. The accuracy score is printed to the console.
