# ==========================================================
# Nama  : Syahrul Hidayatullah
# NIM   :
# Kelas :
# Praktikum 12 - Graph II: Shortest Path
# Materi 1 - Algoritma Dijkstra
# ==========================================================

import heapq

# Weighted graph
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):

    # Menyimpan jarak minimum setiap node
    distances = {node: float('inf') for node in graph}

    # Jarak node awal = 0
    distances[start] = 0

    # Priority queue
    pq = [(0, start)]

    while pq:

        # Mengambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(pq)

        # Mengecek semua tetangga
        for neighbor, weight in graph[current_node].items():

            distance = current_distance + weight

            # Jika ditemukan jarak lebih kecil
            if distance < distances[neighbor]:
                distances[neighbor] = distance

                # Memasukkan ke priority queue
                heapq.heappush(pq, (distance, neighbor))

    return distances

hasil = dijkstra(graph, 'A')

print("Hasil shortest path:")
print(hasil)