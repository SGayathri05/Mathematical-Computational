import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Define a function to fit and predict a linear regression model
def fit_linear_regression(x_train, y_train, x_test):
    # Create a Linear Regression object and fit the training data
    lr = LinearRegression()
    lr.fit(x_train, y_train)

    # Predict the test data
    y_pred = lr.predict(x_test)

    # Return the predicted values
    return y_pred

# Define the Streamlit app
def app():
    st.write("# Simple Linear Regression")
    
    # Upload the data file
    data_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if data_file is not None:
        # Read the data into a Pandas DataFrame
        data = pd.read_csv(data_file)

        # Select the predictor and target variables
        predictor_var = st.selectbox("Select the predictor variable", options=data.columns)
        target_var = st.selectbox("Select the target variable", options=data.columns)

        # Split the data into training and test sets
        train_size = st.slider("Training set size", min_value=0.1, max_value=0.9, value=0.7, step=0.1, format="%f")
        train_size = int(train_size * len(data))
        test_size = len(data) - train_size
        train_data = data[:train_size]
        test_data = data[train_size:]

        # Fit the linear regression model
        x_train = train_data[[predictor_var]]
        y_train = train_data[target_var]
        x_test = test_data[[predictor_var]]
        # y_pred = fit_linear_regression(x_train, y_train, x_test)
       
        lr = LinearRegression()
        lr.fit(x_train, y_train)

        # Predict the test data
        y_pred = lr.predict(x_test)

        # Display the results
        st.write("## Results")
        st.write(f"Predictor variable: {predictor_var}")
        st.write(f"Target variable: {target_var}")
        st.write(f"Training set size: {train_size}")
        st.write(f"Test set size: {test_size}")
        st.write("### Coefficients")
        st.write(lr.coef_)
        st.write("### Predictions")
        st.write(pd.DataFrame({"Actual": test_data[target_var], "Predicted": y_pred}))

# Run the app
if __name__ == "__main__":
    app()
