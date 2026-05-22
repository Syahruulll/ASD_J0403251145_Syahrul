# =======================================
# Syahrul Hidayatullah
# J0403251145
# A/P2
# =======================================


# Adjacency List menggunakan dictionary

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

# Menampilkan adjacency list
print("Adjacency List:")
for node, edges in graph.items():
    print(node, "->", edges)