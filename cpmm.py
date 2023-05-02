import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.title('Critical Path Method')

# Get user input for tasks and durations
num_tasks = st.number_input('How many tasks do you have?', min_value=2, max_value=20, value=5, step=1)

tasks = []
durations = []

for i in range(num_tasks):
    task = st.text_input(f'Task {i+1}')
    duration = st.number_input(f'Duration (in days) for Task {i+1}', min_value=1, value=5)
    tasks.append(task)
    durations.append(duration)

# Create a network graph for the tasks and durations
G = nx.DiGraph()

for i in range(num_tasks):
    G.add_node(tasks[i], duration=durations[i])

# Get user input for task dependencies
for i in range(num_tasks):
    dependencies = st.multiselect(f'What tasks does {tasks[i]} depend on?', tasks[:i])
    for dependency in dependencies:
        G.add_edge(dependency, tasks[i])

# Calculate the critical path and total duration
critical_path = nx.algorithms.dag.dag_longest_path(G)
total_duration = nx.algorithms.dag.dag_longest_path_length(G)

# Display results
st.header('Results')
st.write(f'The critical path is: {critical_path}')
st.write(f'Total Duration Lenght:  {total_duration}')



import streamlit as st 
import networkx as nx 

st.header("CPM")

num_tasks = int(st.number_input("Enter no. of tasks:"))

tasks=[]
durations=[]

for i in range(num_tasks):
    task = st.text_input(f"Enter task{i+1}")
    duration = st.number_input(f"Enter duration {i+1}")
    tasks.append(task)
    durations.append(duration)

G = nx.DiGraph()

for i in range(num_tasks):
        G.add_node(tasks[i],duration=durations[i])

for i in range(num_tasks):
    dependencies = st.multiselect(f"Select dependencies {i+1}:",tasks[:i])
    for j in dependencies:
        G.add_edge(j,tasks[i])

if(st.button("submit:")):
    critical_path = nx.algorithms.dag.dag_longest_path(G)
    total_duration = nx.algorithms.dag.dag_longest_path_length(G)

    st.write("critical path",critical_path)
    st.write("total duration",total_duration)

