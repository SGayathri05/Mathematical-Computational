import streamlit as st
import numpy as np
import networkx as nx
from collections import defaultdict

def cpm(start, end, duration):
    nodes = set(start + end)
    graph = defaultdict(list)
    for s, e, d in zip(start, end, duration):
        graph[s].append((e, d))
        graph[e].append((s, d))
    sources = [node for node in nodes if node not in end]
    sinks = [node for node in nodes if node not in start]
    times = {node: float('inf') for node in nodes}
    times[sources[0]] = 0
    queue = [sources[0]]
    visited = set()
    while queue:
        node = queue.pop(0)
        visited.add(node)
        for neighbor, duration in graph[node]:
            times[neighbor] = min(times[neighbor], times[node] + duration)
            if neighbor not in visited:
                queue.append(neighbor)
    max_time = max(times.values())
    return max_time, times

def draw_graph(start, end, duration):
    nodes = set(start + end)
    graph = defaultdict(list)
    for s, e, d in zip(start, end, duration):
        graph[s].append((e, d))
        graph[e].append((s, d))
    g = nx.DiGraph()
    for node in nodes:
        g.add_node(node)
    for s, neighbors in graph.items():
        for e, d in neighbors:
            g.add_edge(s, e, weight=d)
    pos = nx.spring_layout(g)
    nx.draw_networkx_nodes(g, pos, node_size=800)
    nx.draw_networkx_edges(g, pos)
    nx.draw_networkx_labels(g, pos, font_size=20)
    labels = {(s, e): d for s, neighbors in graph.items() for e, d in neighbors}
    nx.draw_networkx_edge_labels(g, pos, edge_labels=labels, font_size=20)

def main():
    st.title("Critical Path Method (CPM)")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        data = np.genfromtxt(uploaded_file, delimiter=',', dtype='str')
        start = list(data[1:, 0])
        end = list(data[1:, 1])
        duration = list(map(int, data[1:, 2]))
        max_time, times = cpm(start, end, duration)
        st.subheader("Results")
        st.write("Critical path length:", max_time)
        st.write("Activity start and end times:")
        for node, time in times.items():
            st.write(node, ":", time)
        st.subheader("Graphical representation")
        draw_graph(start, end, duration)
        st.pyplot()
    else:
        st.write("Please upload a CSV file")

if __name__ == "__main__":
    main()
