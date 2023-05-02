import streamlit as st
import numpy as np
import pulp


def least_cost_method(costs, supply, demand):
    # Create a linear programming problem
    prob = pulp.LpProblem("Transportation Problem", pulp.LpMinimize)

    # Create decision variables
    decisions = pulp.LpVariable.dicts("Route", ((i, j) for i in range(len(supply)) for j in range(len(demand))), lowBound=0, cat='Integer')

    # Objective function
    prob += pulp.lpSum([costs[i][j] * decisions[(i, j)] for i in range(len(supply)) for j in range(len(demand))])

    # Constraints
    for i in range(len(supply)):
        prob += pulp.lpSum([decisions[(i, j)] for j in range(len(demand))]) == supply[i]
    for j in range(len(demand)):
        prob += pulp.lpSum([decisions[(i, j)] for i in range(len(supply))]) == demand[j]

    # Solve the problem
    prob.solve()

    # Create a matrix to store the results
    result = np.zeros((len(supply), len(demand)))

    # Print the results
    for i in range(len(supply)):
        for j in range(len(demand)):
            result[i][j] = decisions[(i, j)].varValue
            st.write(f"Ship {result[i][j]} units from source {i+1} to destination {j+1} at a cost of {costs[i][j]} per unit.")

    st.write(f"\nTotal cost = ${pulp.value(prob.objective)}")
    st.write("\nOptimal shipping plan:")
    st.write(result)


def main():
    st.title("Least Cost Method")
    st.write("This app solves transportation problems using the Least Cost Method.")
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
        least_cost_method(costs, supply, demand)


if __name__ == "__main__":
    main()
