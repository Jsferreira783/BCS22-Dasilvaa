import heapq

# Create a dictionary to represent the weighted graph
graph = {
    "Home": [("Store A", 7), ("Store B", 14), ("Intersection", 25)],
    "Store A": [("Home", 7), ("Store B", 5)],
    "Store B": [("School", 7)],
    "School": [("Store B", 7), ("Intersection", 7)],
    "Intersection": [("School", 7)]
}

# This function represents Dijkstra's algorithm to find shortest distances and paths
def shortest_path_graph(graph, start, end):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    previous_vertices = {vertex: None for vertex in graph}

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor_vertex, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor_vertex]:
                distances[neighbor_vertex] = distance
                heapq.heappush(priority_queue, (distance, neighbor_vertex))
                previous_vertices[neighbor_vertex] = current_vertex

    shortest_path = []
    while end:
        shortest_path.insert(0, end)
        end = previous_vertices[end]

    return distances, shortest_path

start_vertex = "Home"
end_vertex = "Intersection"
shortest_distances, shortest_path = shortest_path_graph(graph, start_vertex, end_vertex)

print("Shortest Distances:", shortest_distances)
print("Shortest Path:", shortest_path)
