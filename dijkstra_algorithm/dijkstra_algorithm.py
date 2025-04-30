import heapq
import matplotlib.pyplot as plt
import networkx as nx

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

# Manual implementation of Dijkstra's algorithm
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph.nodes}
    previous = {node: None for node in graph.nodes}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_dist, current_node = heapq.heappop(queue)

        if current_dist > distances[current_node]:
            continue

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    # Build shortest paths from previous map
    paths = {}
    for node in graph.nodes:
        path = []
        current = node
        while current is not None:
            path.insert(0, current)
            current = previous[current]
        if distances[node] < float('inf'):
            paths[node] = path
        else:
            paths[node] = []

    return distances, paths

# Compute all pairs shortest paths
print("Shortest paths using custom Dijkstra's algorithm:\n")
for source in G.nodes:
    distances, paths = dijkstra(G, source)
    for target in G.nodes:
        if source != target:
            print(f"{source} → {target}: path = {paths[target]}, total weight = {distances[target]}")

# Visualize the graph
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color="lightgreen",
        node_size=600, font_size=10, edge_color="gray")
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black')
plt.title("Weighted Social Network Graph")
plt.show()
