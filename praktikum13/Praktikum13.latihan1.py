# ==========================================================
# Nama : Syahrul Hidayatullah
# NIM  : Isi NIM
# Kelas: Isi Kelas
# Praktikum 13 - Graph III: Spanning Tree
# File : Praktikum13.latihan1.py
# ==========================================================

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# Menampilkan edge graph
print("Edge pada graph:")

for edge in edges:
    print(edge)

# Menampilkan spanning tree
print("\nSpanning Tree:")

for edge in spanning_tree:
    print(edge)

# Menampilkan jumlah edge
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# ==========================================================
# Jawaban Analisis:
#
# 1. Graph awal memiliki cycle dan edge lebih banyak,
#    sedangkan spanning tree hanya memiliki edge yang
#    diperlukan untuk menghubungkan semua node.
#
# 2. Spanning tree tidak boleh memiliki cycle karena
#    cycle menyebabkan penggunaan edge berlebih dan
#    membuat graph tidak efisien.
#
# 3. Jumlah edge spanning tree lebih sedikit karena
#    spanning tree hanya membutuhkan n-1 edge untuk
#    menghubungkan seluruh node.
# ==========================================================