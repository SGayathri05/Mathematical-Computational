import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def main():
    st.title("Multiple Linear Regression")

    # Upload CSV file
    st.sidebar.title("Upload CSV file")
    uploaded_file = st.sidebar.file_uploader("", type="csv")
    if uploaded_file is not None:
        # Read CSV file
        df = pd.read_csv(uploaded_file)

        st.header("Overall Scatter Plot")
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, ax=ax)
        st.pyplot(fig)

        # Select target variable
        st.sidebar.title("Select target variable")
        target_col = st.sidebar.selectbox("", df.columns)

        # Select predictor variables
        st.sidebar.title("Select predictor variables")
        predictor_cols = st.sidebar.multiselect("", df.columns)

        # Split data into train and test sets
        X_train, X_test, y_train, y_test = train_test_split(
            df[predictor_cols], df[target_col], test_size=0.3, random_state=0)

        # Perform multiple linear regression on train data
        reg = LinearRegression().fit(X_train, y_train)

        # Compute predicted values for train and test data
        y_train_pred = reg.predict(X_train)
        y_test_pred = reg.predict(X_test)

        # Compute RMSE for train and test data
        rmse_train = np.sqrt(mean_squared_error(y_train, y_train_pred))
        rmse_test = np.sqrt(mean_squared_error(y_test, y_test_pred))

        #Display scatter plot of target variable and predictor variables
        # st.header("Scatter Plot")
        # fig, ax = plt.subplots()
        # sns.scatterplot(x=target_col, y=predictor_cols[0], data=df, ax=ax)
        # st.pyplot(fig)

        st.header("Scatter Plot")
        fig, ax = plt.subplots()
        sns.scatterplot(x=target_col, y=predictor_cols[0], data=df, ax=ax)
        for col in predictor_cols:
                    sns.regplot(x=col, y=target_col, data=df, ax=ax, scatter=False)
                    st.pyplot(fig)

        # Display regression equation and coefficient of determination
        st.header("Regression Equation and Coefficient of Determination")
        st.write("Regression Equation: {} = {} + ".format(target_col, reg.intercept_) + " + ".join(["{}*{}".format(round(reg.coef_[i],2), predictor_cols[i]) for i in range(len(predictor_cols))]))
        st.write("Coefficient of Determination (R^2): {}".format(reg.score(X_train, y_train)))

        # Display RMSE for train and test data
        st.header("RMSE")
        st.write("RMSE for Train Data: {}".format(round(rmse_train, 2)))
        st.write("RMSE for Test Data: {}".format(round(rmse_test, 2)))

        # fig, ax = plt.subplots()
        # ax.scatter(x, y)
        # ax.plot(x, y_pred, color='red')
        # ax.set_xlabel("x")
        # ax.set_ylabel("y")
        # ax.set_title("Scatter plot with regression line")
        # st.pyplot(fig)

    else:
        st.warning("Please upload a CSV file")

if __name__ == '__main__':
    main()
