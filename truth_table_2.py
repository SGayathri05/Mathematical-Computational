import streamlit as st
import itertools

# Define a function to generate a truth table
import streamlit as st
import itertools

# Define a function to generate a truth table
def truth_table(n, f):
    inputs = list(itertools.product([0, 1], repeat=n))
    outputs = [f(*inputs[i]) for i in range(2 ** n)]
    return inputs, outputs

# Define the logic gates
def and_gate(*inputs):
    return int(all(inputs))

def or_gate(*inputs):
    return int(any(inputs))

def not_gate(x):
    return int(not x)

def xor_gate(x, y):
    return int(x != y)

# Create a Streamlit web app
st.title("Truth table generator")

# Get the number of inputs from the user
n = st.slider("Number of inputs", min_value=1, max_value=5, value=2, step=1)

# Display the truth tables for all the basic logic gates
st.header("AND gate")
inputs, outputs = truth_table(n, and_gate)
table_data = [[" ".join(str(x) for x in input), output] for input, output in zip(inputs, outputs)]
st.table([["Inputs", "Output"]] + table_data)

st.header("OR gate")
inputs, outputs = truth_table(n, or_gate)
table_data = [[" ".join(str(x) for x in input), output] for input, output in zip(inputs, outputs)]
st.table([["Inputs", "Output"]] + table_data)

st.header("NOT gate")
inputs, outputs = truth_table(1, not_gate)
table_data = [[" ".join(str(x) for x in input), output] for input, output in zip(inputs, outputs)]
st.table([["Input", "Output"]] + table_data)

st.header("XOR gate")
inputs, outputs = truth_table(n, xor_gate)
table_data = [[" ".join(str(x) for x in input), output] for input, output in zip(inputs, outputs)]
st.table([["Inputs", "Output"]] + table_data)
