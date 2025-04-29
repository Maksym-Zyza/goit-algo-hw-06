import networkx as nx
from collections import deque
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes
people = ["Luke", "Leia", "Han", "Aragorn", "Legolas", "Neo"]
G.add_nodes_from(people)

# Add edges (friendship connections)
friendships = [
    ("Luke", "Leia"),
    ("Luke", "Han"),
    ("Leia", "Han"),
    ("Han", "Aragorn"),
    ("Leia", "Aragorn"),
    ("Aragorn", "Legolas"),
    ("Legolas", "Neo"),
    ("Aragorn", "Neo"),
]
G.add_edges_from(friendships)


def dfs_path(graph, start, goal):
    """DFS Implementation"""
    # Stack for DFS
    stack = [(start, [start])]
    visited = set()

    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            # Add neighbors to stack
            for neighbor in graph.neighbors(vertex):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return None  # No path found


def bfs_path(graph, start, goal):
    """BFS Implementation"""
    # Queue for BFS
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (vertex, path) = queue.popleft()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            # Add neighbors to queue
            for neighbor in graph.neighbors(vertex):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None  # No path found


# Find paths from Luke to Neo
start_node = "Luke"
goal_node = "Neo"

# Run DFS
dfs_result = dfs_path(G, start_node, goal_node)
print(f"DFS path from {start_node} to {goal_node}: {dfs_result}")

# Run BFS
bfs_result = bfs_path(G, start_node, goal_node)
print(f"BFS path from {start_node} to {goal_node}: {bfs_result}")

# Visualize the graph
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightblue",
    node_size=500,
    font_size=12,
    edge_color="gray",
)
plt.title("Social Network Graph")
plt.show()
