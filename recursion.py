import streamlit as st

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    st.title("Factorial Calculator")
    n = st.number_input("Enter a number:", min_value=0, step=1)
    result = factorial(n)
    st.write(f"The factorial of {n} is {result}")

if __name__ == "__main__":
    main()
