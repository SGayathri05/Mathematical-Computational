import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import streamlit as st

# Add a title
st.title('Multiple Linear Regression')

# Upload the dataset
data_file = st.file_uploader('Upload a CSV file', type='csv')

# Load the dataset dynamically
if data_file is not None:
    data = pd.read_csv(data_file)

    # Preprocess the data
    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # Fit the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Print the results
    st.subheader('Exploratory Data Analysis')
    st.write(data.head())
    st.subheader('Multiple Linear Regression Results')
    st.write('Coefficients:', model.coef_)
    st.write('Intercept:', model.intercept_)
    st.write('Mean Squared Error:', np.mean((y_pred - y_test) ** 2))
    st.write('R-squared:', model.score(X_test, y_test))
