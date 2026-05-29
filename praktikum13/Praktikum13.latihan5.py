# ==========================================================
# Nama : Syahrul Hidayatullah
# NIM  : Isi NIM
# Kelas: Isi Kelas
# Praktikum 13 - Graph III: Spanning Tree
# File : Praktikum13.latihan5.py
# ==========================================================

# Kasus yang dipilih:
# Jaringan Jalan Antar Kota

# Menggunakan Algoritma Prim

import heapq

# Representasi weighted graph
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Jakarta': {'Bogor': 5, 'Depok': 3, 'Bandung': 6},
    'Depok': {'Bogor': 2, 'Jakarta': 3, 'Bandung': 4},
    'Bandung': {'Jakarta': 6, 'Depok': 4}
}

# Fungsi Prim
def prim(graph, start):

    visited = set([start])

    edges = []

    # Menambahkan edge awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:

        weight, u, v = heapq.heappop(edges)

        if v not in visited:

            visited.add(v)

            mst.append((u, v, weight))

            total_weight += weight

            # Menambahkan edge baru
            for neighbor, w in graph[v].items():

                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

# Menjalankan Prim
mst, total = prim(graph, 'Bogor')

# Menampilkan hasil
print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot =", total)

# ==========================================================
# Jawaban Analisis:
#
# 1. Kasus yang dipilih adalah jaringan jalan antar kota.
#
# 2. Algoritma yang digunakan adalah Prim.
#
# 3. Edge yang dipilih dalam MST:
#    - Bogor - Depok
#    - Depok - Jakarta
#    - Depok - Bandung
#
# 4. Total bobot MST adalah 9.
#
# 5. Edge tertentu tidak dipilih karena memiliki bobot
#    lebih besar dan dapat menyebabkan jalur tidak efisien.
# ==========================================================