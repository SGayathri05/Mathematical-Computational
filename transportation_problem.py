import streamlit as st
import numpy as np
import pandas as pd
import pulp

def solve_transportation_problem(costs, supply, demand):
    """
    Solves the transportation problem using the given cost, supply, and demand data.
    Returns a tuple (x, total_cost), where x is the optimal transportation matrix and
    total_cost is the total cost of transportation.
    """
    m, n = len(supply), len(demand)
    prob = pulp.LpProblem("Transportation Problem", pulp.LpMinimize)

    # Define decision variables
    x = []
    for i in range(m):
        x.append([])
        for j in range(n):
            x[i].append(pulp.LpVariable(f"x_{i}_{j}", lowBound=0))

    # Define objective function
    total_cost = 0
    for i in range(m):
        for j in range(n):
            total_cost += costs[i,j] * x[i][j]
    prob += total_cost

    # Define supply constraints
    for i in range(m):
        prob += pulp.lpSum(x[i][j] for j in range(n)) == supply[i]

    # Define demand constraints
    for j in range(n):
        prob += pulp.lpSum(x[i][j] for i in range(m)) == demand[j]

    # Solve the problem
    prob.solve()

    # Convert the solution to a numpy array
    x = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            x[i][j] = pulp.value(x[i][j])

    # Return the solution
    return x, pulp.value(total_cost)

def main():
    st.title("Vogel Approximation Method Solver")

    # Get the cost, supply, and demand data from the user
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

    # Solve the problem
    x, total_cost = solve_transportation_problem(costs, supply, demand)

    # Display the solution
    # st.write("Optimal transportation:")
    # st.write(pd.DataFrame(x))
    st.write("Total cost of transportation: Rs", total_cost)

if __name__ == '__main__':
    main()
