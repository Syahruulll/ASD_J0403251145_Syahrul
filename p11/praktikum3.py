# =======================================
# Syahrul Hidayatullah
# J0403251145
# A/P2
# =======================================

# Adjacency Matrix
matrix = [
    [0,1,1,0],
    [1,0,1,0],
    [1,1,0,1],
    [0,0,1,0]
]

# Nama node
nodes = ["A", "B", "C", "D"]

# Konversi matrix ke adjacency list
graph = {}

for i in range(len(matrix)):
    connections = []

    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            connections.append(nodes[j])

    graph[nodes[i]] = connections

# Menampilkan adjacency list
print("Adjacency List:")
for node, edges in graph.items():
    print(node, "->", edges)