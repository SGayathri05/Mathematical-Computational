import streamlit as st

def master_theorem(a, b, f, n):
    if n == 0:
        return f(0)
    elif n > 0:
        return a * master_theorem(a, b, f, n // b) + f(n)

def main():
    st.title("Master Theorem Recursion")

    st.write("This program uses the Master Theorem to solve recurrence relations of the form:")
    st.latex("T(n) = a T(\lfloor n/b \rfloor) + f(n)")

    a = st.number_input("Enter the value of a", min_value=1, step=1)
    b = st.number_input("Enter the value of b", min_value=2, step=1)
    f_input = st.text_input("Enter the function f(n)", "n")
    try:
        f = lambda n: eval(f_input, {'n': n})
    except:
        st.error("Invalid function definition for f(n)")
        return

    n = st.number_input("Enter the value of n", min_value=0, step=1)

    if st.button("Solve"):
        result = master_theorem(a, b, f, n)
        st.subheader("Result")
        st.write(f"T({n}) = {result}")

if __name__ == "__main__":
    main()
