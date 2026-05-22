# =======================================
# Syahrul Hidayatullah
# J0403251145
# A/P2
# =======================================


nodes = ["Router1", "Switch1", "Switch2", "PC1", "PC2", "Server1"]

# Adjacency List
graph = {
    "Router1": ["Switch1", "Switch2"],
    "Switch1": ["Router1", "PC1", "PC2"],
    "Switch2": ["Router1", "PC2", "Server1"],
    "PC1": ["Switch1"],
    "PC2": ["Switch1", "Switch2"],
    "Server1": ["Switch2"]
}

# Adjacency Matrix
matrix = [
#R1 S1 S2 P1 P2 SV
 [0, 1, 1, 0, 0, 0], # Router1
 [1, 0, 0, 1, 1, 0], # Switch1
 [1, 0, 0, 0, 1, 1], # Switch2
 [0, 1, 0, 0, 0, 0], # PC1
 [0, 1, 1, 0, 0, 0], # PC2
 [0, 0, 1, 0, 0, 0]  # Server1
]

# Menampilkan node
print("=== Nama Node ===")
for node in nodes:
    print(node)

# Menampilkan hubungan antar node
print("\n=== Hubungan Antar Node ===")
for node, edges in graph.items():
    print(node, "->", edges)

# Menampilkan adjacency list
print("\n=== Adjacency List ===")
print(graph)

# Menampilkan adjacency matrix
print("\n=== Adjacency Matrix ===")
for row in matrix:
    print(row)