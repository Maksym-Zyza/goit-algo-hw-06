import networkx as nx
import matplotlib.pyplot as plt

# Create a weighted undirected graph
G = nx.Graph()

# Add nodes (people)
people = ["Luke", "Leia", "Han", "Aragorn", "Legolas", "Neo"]
G.add_nodes_from(people)

# Add edges with weights (e.g., connection strength or distance)
weighted_friendships = [
    ("Luke", "Leia", 2),
    ("Luke", "Han", 1),
    ("Leia", "Han", 2),
    ("Han", "Aragorn", 3),
    ("Leia", "Aragorn", 2),
    ("Aragorn", "Legolas", 2),
    ("Legolas", "Neo", 4),
    ("Aragorn", "Neo", 1),
]

# Add weighted edges to the graph
for u, v, weight in weighted_friendships:
    G.add_edge(u, v, weight=weight)

# Use Dijkstra's algorithm to find the shortest paths between all pairs of nodes
shortest_paths = dict(nx.all_pairs_dijkstra_path(G, weight='weight'))
shortest_lengths = dict(nx.all_pairs_dijkstra_path_length(G, weight='weight'))

# Print the shortest paths and their total weights
print("Shortest paths using Dijkstra's algorithm:\n")
for source in shortest_paths:
    for target in shortest_paths[source]:
        path = shortest_paths[source][target]
        length = shortest_lengths[source][target]
        print(f"{source} → {target}: path = {path}, total weight = {length}")

# Visualize the graph with edge weights
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G, seed=42)  # Position layout for consistent graph appearance
nx.draw(
    G, pos, with_labels=True, node_color="lightgreen",
    node_size=600, font_size=10, edge_color="gray"
)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black')
plt.title("Weighted Social Network Graph")
plt.show()
