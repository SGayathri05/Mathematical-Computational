import streamlit as st
import numpy as np

def north_west_corner_method(supply, demand, cost):
    supply = np.array(supply)
    demand = np.array(demand)
    cost = np.array(cost)
    m, n = cost.shape
    allocation = np.zeros((m, n))
    i, j = 0, 0
    while i < m and j < n:
        quantity = min(supply[i], demand[j])
        allocation[i, j] = quantity
        supply[i] -= quantity
        demand[j] -= quantity
        if supply[i] == 0:
            i += 1
        if demand[j] == 0:
            j += 1
    return allocation
  
def main():
    st.title("North-West Corner Method for Transportation Problem")
    m = st.number_input("Enter the number of sources (m):", min_value=1, step=1)
    n = st.number_input("Enter the number of destinations (n):", min_value=1, step=1)
    supply_str = st.text_input("Enter the supply for each source (separated by spaces):")
    demand_str = st.text_input("Enter the demand for each destination (separated by spaces):")
    cost_str = [st.text_input(f"Enter the cost matrix for source {i+1} (separated by spaces):") for i in range(m)]
    if not supply_str or not demand_str or not all(cost_str):
        st.error("Input cannot be empty")
        return
    supply = np.array(supply_str.split(), dtype=int)
    demand = np.array(demand_str.split(), dtype=int)
    cost = np.zeros((m, n))
    for i in range(m):
        cost[i] = np.array(cost_str[i].split(), dtype=int)
    if supply.shape != (m,) or demand.shape != (n,) or cost.shape != (m, n):
        st.error("Input format is incorrect")
        return
    allocation = north_west_corner_method(supply, demand, cost)
    st.write("Allocation matrix:\n", allocation)
    st.write("Total cost:", np.sum(allocation * cost))

if __name__ == "__main__":
    main()
