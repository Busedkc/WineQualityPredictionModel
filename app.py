import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import streamlit as st 

#load the wine dataset 
wine = pd.read_csv('winequality-red.csv')

#Create the predictor (X) and target (y) variables
X = wine.drop('quality', axis=1)
y = wine['quality'].apply(lambda yval:1 if yval >= 7 else 0)

X_train, X_test, Y_train, Y_test = train_test_split(X,y, test_size=0.2, random_state=3)
#Train the Random Forest Classifier model
model = RandomForestClassifier()
model.fit(X_train, Y_train)
# accuracy on the test data
X_test_prediction = model.predict(X_test)
print(accuracy_score(X_test_prediction, Y_test))

#web app
st.title("Wine Quality Prediction Model")
input_text = st.text_input("Enter all Wine Features")
input_text_list = input_text.split(',')
features = np.asarray(input_text_list)
prediction = model.predict(features.reshape(1,-1))
if prediction[0] == 1:
    st.write("Good Quality Wine")
else:
    st.write("Bad Quality Wine")