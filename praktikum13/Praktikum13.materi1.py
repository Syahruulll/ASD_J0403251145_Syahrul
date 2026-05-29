# ==========================================================
# Nama : Syahrul Hidayatullah
# NIM  : Isi NIM
# Kelas: Isi Kelas
# Praktikum 13 - Graph III: Spanning Tree
# File : Praktikum13.materi1.py
# ==========================================================

# Materi 1 - Implementasi Sederhana Kruskal

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0

# Menyimpan node yang sudah terhubung
connected = set()

# Proses memilih edge
for weight, u, v in edges:

    # Edge dipilih jika tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight

        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total_weight)

# ==========================================================
# Penjelasan:
# Algoritma Kruskal bekerja dengan memilih edge dengan
# bobot terkecil terlebih dahulu tanpa membentuk cycle.
# ==========================================================