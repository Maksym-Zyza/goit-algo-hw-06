import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Add nodes
people = ["Luke", "Leia", "Han", "Aragorn", "Legolas", "Neo"]
G.add_nodes_from(people)

# Add edges
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

# Analyze graph properties
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")
print("\nDegrees:")
for node, degree in degrees.items():
    print(f"{node}: {degree}")

# Graph visualization
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=500,
    font_size=12,
    node_color="lightcoral",
    edge_color="gray",
)
plt.title("Movie Characters Social Network")
plt.show()
