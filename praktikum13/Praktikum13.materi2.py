# ==========================================================
# Nama : Syahrul Hidayatullah
# NIM  : Isi NIM
# Kelas: Isi Kelas
# Praktikum 13 - Graph III: Spanning Tree
# File : Praktikum13.materi2.py
# ==========================================================

# Materi 2 - Implementasi Algoritma Prim

import heapq

# Representasi weighted graph
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

# Fungsi algoritma Prim
def prim(graph, start):

    # Node yang sudah dikunjungi
    visited = set([start])

    # Menyimpan edge sementara
    edges = []

    # Memasukkan edge awal ke priority queue
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    # Proses pemilihan edge
    while edges:

        weight, u, v = heapq.heappop(edges)

        if v not in visited:

            visited.add(v)

            mst.append((u, v, weight))

            total_weight += weight

            # Memasukkan edge baru
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

# Menjalankan Prim
mst, total = prim(graph, 'A')

# Menampilkan hasil
print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot =", total)

# ==========================================================
# Penjelasan:
# Algoritma Prim membangun spanning tree mulai dari
# satu node awal kemudian memilih edge terkecil berikutnya.
# ==========================================================