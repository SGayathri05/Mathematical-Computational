import streamlit as st
import numpy as np

# @st.cache(suppress_st_warning=True)
def vogel_method(costs, supply, demand):
    m, n = len(supply), len(demand)
    x = np.zeros((m, n))
    while np.any(supply) > 0 and np.any(demand) > 0:
        u, v = np.zeros(m), np.zeros(n)
        for i in range(m):
            row = sorted([(costs[i, j], j) for j in range(n) if x[i, j] == 0])
            if row:
                u[i] = row[0][0] - row[1][0] if len(row) > 1 else row[0][0]
        for j in range(n):
            col = sorted([(costs[i, j], i) for i in range(m) if x[i, j] == 0])
            if col:
                v[j] = col[0][0] - col[1][0] if len(col) > 1 else col[0][0]
        i, j = np.unravel_index(np.argmax(u[:, None] + v, axis=None), (m, n))
        amount = min(supply[i], demand[j])
        x[i, j] = amount
        supply[i] -= amount
        demand[j] -= amount
    return x
def main():
    st.title("Vogel's Approximation Method")
    st.write("This app solves transportation problems using Vogel's Approximation Method.")
    st.write("To get started, enter the number of sources, the number of destinations, and the cost matrix.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        m = st.number_input("Enter the number of sources (supply):", min_value=1, step=1)
        n = st.number_input("Enter the number of destinations (demand):", min_value=1, step=1)
        
        costs = np.zeros((m, n))
        for i in range(m):
            costs[i] = st.text_input(f"Enter the costs for source {i+1} (separated by spaces):").split()
            if len(costs[i]) != n:
                st.error(f"Input format is incorrect for source {i+1}")
                return
        
        supply = np.zeros(m)
        for i in range(m):
            supply[i] = st.number_input(f"Enter the supply for source {i+1}:", min_value=0, step=1)
        
        demand = np.zeros(n)
        for j in range(n):
            demand[j] = st.number_input(f"Enter the demand for destination {j+1}:", min_value=0, step=1)
        
        st.write("Computing the optimal transportation...")
        x = vogel_method(costs, supply, demand)
        st.write("Optimal transportation:")
        st.write(x)

if __name__ == "__main__":
    main()