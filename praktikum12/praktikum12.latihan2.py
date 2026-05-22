# ==========================================================
# Nama  : Syahrul Hidayatullah
# NIM   :
# Kelas :
# Praktikum 12 - Graph II: Shortest Path
# Latihan 2 - Dijkstra
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

    distances = {node: float('inf') for node in graph}

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

hasil = dijkstra(graph, 'A')

print("Jarak terpendek dari node A:")

for node, distance in hasil.items():
    print(node, "=", distance)

# ==========================================================
# Jawaban Analisis:
#
# 1. Jarak A ke B adalah 4
#
# 2. Jarak A ke C adalah 2
#
# 3. Jarak A ke D adalah 3
#
# 4. Karena jalur melalui C memiliki total bobot
#    lebih kecil yaitu 2 + 1 = 3
#
# 5. Priority queue digunakan untuk mengambil
#    node dengan jarak terkecil terlebih dahulu
#
# 6. Karena Dijkstra tidak dapat menghitung
#    bobot negatif dengan benar
# ==========================================================