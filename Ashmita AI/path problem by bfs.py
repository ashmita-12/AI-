from collections import deque
def bfs_shortest_path(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])
    while queue:
        current_node, path = queue.popleft()
        if current_node == goal:
            return path
        visited.add(current_node)     
        for neighbor, _ in graph.get(current_node, {}).items():
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
# Define the map graph
map_graph = {
    'A': {'B': 1, 'D': 3},
    'B': {'A': 1, 'C': 2, 'E': 1},
    'C': {'B': 2, 'F': 1},
    'D': {'A': 3, 'E': 2},
    'E': {'B': 1, 'D': 2, 'F': 1},
    'F': {'C': 1, 'E': 1}
}
# Find the shortest path from A to F
shortest_path_A_to_F = bfs_shortest_path(map_graph, 'A', 'F')
print("Shortest path from A to F:", shortest_path_A_to_F)
