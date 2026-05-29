# ==========================================================
# Nama : Syahrul Hidayatullah
# NIM  : Isi NIM
# Kelas: Isi Kelas
# Praktikum 13 - Graph III: Spanning Tree
# File : Praktikum13.latihan4.py
# ==========================================================

# Studi Kasus: Jaringan Kabel Antar Gedung
# Menggunakan Algoritma Kruskal

# Daftar edge
edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

# Mengurutkan edge
edges.sort()

mst = []
total_cost = 0

connected = set()

# Proses Kruskal
for weight, u, v in edges:

    if u not in connected or v not in connected:

        mst.append((u, v, weight))

        total_cost += weight

        connected.add(u)
        connected.add(v)

# Menampilkan hasil
print("Jaringan Kabel Minimum:")

for edge in mst:
    print(edge)

print("Total biaya minimum =", total_cost)

# ==========================================================
# Jawaban Analisis:
#
# 1. Algoritma yang digunakan adalah Kruskal.
#
# 2. Edge yang dipilih:
#    - GedungC - GedungD
#    - GedungA - GedungC
#    - GedungB - GedungD
#
# 3. Total biaya minimum adalah 6.
#
# 4. MST cocok digunakan karena dapat menghubungkan
#    seluruh gedung dengan biaya pemasangan minimum.
# ==========================================================