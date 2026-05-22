# ==========================================================
# Nama  : Syahrul Hidayatullah
# NIM   :
# Kelas :
# Praktikum 12 - Graph II: Shortest Path
# Materi 2 - Algoritma Bellman Ford
# ==========================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak node awal = 0
    distances[start] = 0

    # Relaksasi edge sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):

        for node in graph:

            for neighbor, weight in graph[node].items():

                if distances[node] + weight < distances[neighbor]:

                    distances[neighbor] = distances[node] + weight

    return distances

hasil = bellman_ford(graph, 'A')

print("Hasil shortest path:")
print(hasil)