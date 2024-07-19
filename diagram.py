import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Define nodes
nodes = [
    "Flask Application",
    "/ (home)",
    "/face_mouse",
    "Initialize variables",
    "Start an infinite loop",
    # Add more nodes as needed
]

# Define edges (connections between nodes)
edges = [
    ("Flask Application", "/ (home)"),
    ("Flask Application", "/face_mouse"),
    ("/face_mouse", "Initialize variables"),
    ("/face_mouse", "Start an infinite loop"),
    # Add more edges as needed
]

# Add nodes and edges to the graph
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Create a layout for the nodes
pos = nx.spring_layout(G)

# Draw the graph
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, font_color="black")

# Customize the plot, e.g., remove axis labels and set aspect ratio
plt.axis("off")
plt.gca().set_aspect('equal')

# Display the diagram
plt.show()