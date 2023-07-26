import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

def main():
    st.title("Linear Regression")

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

        # Select columns for regression
        st.sidebar.title("Select columns for regression")
        x_col = st.sidebar.selectbox("Choose X variable", df.columns)
        y_col = st.sidebar.selectbox("Choose Y variable", df.columns)       

        # Perform linear regression
        X = df[x_col].values.reshape(-1, 1)
        y = df[y_col].values.reshape(-1, 1)
        lr = LinearRegression().fit(X, y)

        # Display regression equation and coefficient of determination
        st.header("Regression Equation")
        st.write("y = {:.2f}x + {:.2f}".format(lr.coef_[0][0], lr.intercept_[0]))
        st.write("R^2 = {:.2f}".format(lr.score(X, y)))        

        # Display scatter plot and regression line
        st.header("Scatter Plot without Regression Line")
        fig, ax = plt.subplots()
        sns.scatterplot(x=x_col, y=y_col, data=df, ax=ax)
        st.pyplot(fig)

        st.header("Scatter Plot with Regression Line")
        sns.regplot(x=x_col, y=y_col, data=df, ax=ax)
        st.pyplot(fig)

    else:
        st.warning("Please upload a CSV file")

if __name__ == '__main__':
    main()
