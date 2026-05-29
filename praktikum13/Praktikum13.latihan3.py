# ==========================================================
# Nama : Syahrul Hidayatullah
# NIM  : Isi NIM
# Kelas: Isi Kelas
# Praktikum 13 - Graph III: Spanning Tree
# File : Praktikum13.latihan3.py
# ==========================================================

import heapq

# Weighted graph
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

# Fungsi Prim
def prim(graph, start):

    visited = set([start])

    edges = []

    # Memasukkan edge awal
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
mst, total = prim(graph, 'A')

# Menampilkan hasil
print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot =", total)

# ==========================================================
# Jawaban Analisis:
#
# 1. Node awal yang digunakan adalah A.
#
# 2. Edge pertama yang dipilih adalah A-C
#    karena memiliki bobot paling kecil.
#
# 3. Prim menentukan edge berikutnya dengan memilih
#    edge berbobot minimum dari node yang sudah dikunjungi.
#
# 4. Total bobot MST yang dihasilkan adalah 6.
#
# 5. Perbedaan Prim dan Kruskal:
#    - Prim fokus membangun tree dari node awal.
#    - Kruskal fokus memilih edge global terkecil.
# ==========================================================