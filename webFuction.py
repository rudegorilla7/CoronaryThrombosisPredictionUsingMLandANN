import streamlit as st
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix



@st.cache
def load_data():
    """This function returns the preprocessed data"""

    # Load the Diabetes dataset into DataFrame.
    df = pd.read_csv('heart.csv.txt')

    # Rename the column names in the DataFrame.

    # Perform feature and target split
    X = df[
        ["male","age","currentSmoker","cigsPerDay","BPMeds","prevalentStroke","prevalentHyp","diabetes","totChol","sysBP","diaBP","BMI","heartRate","glucose"]]
    y = df["TenYearCHD"]

    return df, X, y


@st.cache()
def train_model(X, y):
    """This function trains the model and return the model and model score"""
    # Splitting the data into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # Create the model
    ann = Sequential()
    ann.add(Dense(activation='relu',input_dim = 13,units = 13, kernel_initializer = "uniform"))
    ann.add(Dense(activation = "relu", units = 14,kernel_initializer = "uniform"))
    ann.add(Dense(activation = "sigmoid", units = 1,kernel_initializer = "uniform"))
    ann.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Fit the data on model
    ann.fit(X, y, batch_size=32, epochs=100)
    # Get the model score
    score = ann.score(X, y)

    # Return the values
    return ann, score

#def predict(X, y, features):
    # Get model and model score
    #model, score = train_model(X, y)
    # Predict the value
    #prediction = model.predict(np.array(features).reshape(1, -1))

    #return prediction, score

def predict(X, y, features):
    # Get model and model score
    ann, score = train_model(X, y)
    # Predict the value
    prediction = ann.predict(np.array(features))
    return prediction, score

