import streamlit as st
import numpy as np
from scipy.optimize import linear_sum_assignment

def assignment_problem(cost_matrix):
    # Solve the assignment problem using the Hungarian algorithm
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    
    # Calculate the total cost
    total_cost = cost_matrix[row_ind, col_ind].sum()
    
    # Return the row and column indices and the total cost
    return row_ind, col_ind, total_cost

# Set up the Streamlit app
st.title("Assignment Problem Solver")

# Get the number of rows and columns
n_rows = st.number_input("Number of rows", min_value=1, step=1)
n_cols = st.number_input("Number of columns", min_value=1, step=1)

# Get the cost matrix
cost_matrix = []
for i in range(n_rows):
    row = st.text_input(f"Row {i+1} costs (separated by spaces)", key=f"row_{i}")
    row = [int(x) for x in row.split()]
    if len(row) != n_cols:
        st.error(f"Row {i+1} must have exactly {n_cols} costs")
        cost_matrix = None
        break
    cost_matrix.append(row)

# If the cost matrix is valid, solve the assignment problem
if cost_matrix is not None:
    cost_matrix = np.array(cost_matrix)
    row_ind, col_ind, total_cost = assignment_problem(cost_matrix)
    
    # Display the results
    st.write("Optimal assignment:")
    for i, j in zip(row_ind, col_ind):
        st.write(f"Row {i+1} -> Column {j+1}")
    st.write(f"Total cost: {total_cost}")

    
#-------------------------------------------------------------------------------------------------------------------

#  NOTE THIS IS SECOND SOLUTION FOR THE SAME ASSIGNMENT PROBLEM:


import streamlit as st 
from scipy.optimize import linear_sum_assignment 
import numpy as np 

st.header("Assignment problem")

n = int(st.number_input("Enter no. of jobs/workers"))

cost_matrix=np.zeros((n,n))

for i in range(n):
    for j in range(n):
        cost_matrix[i,j]=st.number_input(f"Enter cost of worker{i+1} to do job{j+1}")

r,c=linear_sum_assignment(cost_matrix)
min_cost = cost_matrix[r,c].sum()
if(st.button("assign")):
    for i in range(n):
        st.write(f"Work{i+1} is assigned to job{c[i]+1} with cost = {cost_matrix[i,c[i]]}")

    st.write(f"min cost {min_cost}")

