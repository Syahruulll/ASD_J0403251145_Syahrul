# ==========================================================
# Nama  : Syahrul Hidayatullah
# NIM   :
# Kelas :
# Praktikum 12 - Graph II: Shortest Path
# Latihan 1
# ==========================================================

# Representasi weighted graph
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menghitung total bobot jalur
jalur_1 = graph['A']['B'] + graph['B']['D']
jalur_2 = graph['A']['C'] + graph['C']['D']

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

# Menentukan jalur terpendek
if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

# ==========================================================
# Jawaban Analisis:
#
# 1. Total bobot jalur A -> B -> D adalah 9
#
# 2. Total bobot jalur A -> C -> D adalah 3
#
# 3. Jalur terpendek adalah A -> C -> D
#
# 4. Karena shortest path ditentukan berdasarkan
#    total bobot terkecil, bukan jumlah edge.
# ==========================================================