# =======================================
# Syahrul Hidayatullah
# J0403251145
# A/P2
# =======================================

# Node graph
nodes = [0, 1, 2, 3]

# Adjacency Matrix
matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

# Menampilkan matrix
print("Adjacency Matrix:")
for row in matrix:
    print(row)

# Penjelasan setiap baris
print("\nPenjelasan:")
print("Baris 0 : Node 0 terhubung ke node 1 dan 2")
print("Baris 1 : Node 1 terhubung ke node 0, 2, dan 3")
print("Baris 2 : Node 2 terhubung ke node 0, 1, dan 3")
print("Baris 3 : Node 3 terhubung ke node 1 dan 2")