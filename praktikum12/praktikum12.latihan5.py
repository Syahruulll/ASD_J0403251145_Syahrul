# ==========================================================
# Nama  : Syahrul Hidayatullah
# NIM   :
# Kelas :
# Praktikum 12 - Graph II: Shortest Path
# Latihan 5 - Studi Kasus Kota
# ==========================================================

import heapq

# Weighted graph antar kota
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

def dijkstra(graph, start):

    # Semua jarak awal tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak awal = 0
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():

            distance = current_distance + weight

            if distance < distances[neighbor]:

                distances[neighbor] = distance

                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Node awal
start_node = 'Bogor'

hasil = dijkstra(graph, start_node)

print("Jarak terpendek dari Bogor:")

for kota, jarak in hasil.items():
    print(f"Bogor -> {kota} = {jarak}")

# ==========================================================
# Jawaban Analisis:
#
# 1. Node awal yang digunakan adalah Bogor
#
# 2. Node dengan jarak paling kecil adalah Depok
#
# 3. Node dengan jarak paling besar adalah Bandung
#
# 4. Dijkstra bekerja dengan memilih node
#    dengan jarak terkecil terlebih dahulu,
#    lalu memperbarui jarak ke node lain
#    sampai semua node selesai diproses
# ==========================================================