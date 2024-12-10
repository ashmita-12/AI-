import heapq
def heuristic(node, goal):
    # For simplicity, we assume straight-line distance as the heuristic
    # In a real-world scenario, you might need a more sophisticated heuristic
    return abs(ord(node) - ord(goal))
def astar_shortest_path(graph, start, goal):
    visited = set()
    queue = [(0, start, [start])]
    while queue:
        (cost, current_node, path) = heapq.heappop(queue) 
        if current_node == goal:
            return path
        if current_node not in visited:
            visited.add(current_node)
            for neighbor, edge_cost in graph.get(current_node, {}).items():
                if neighbor not in visited:
                    new_cost = cost + edge_cost
                    priority = new_cost + heuristic(neighbor, goal)
                    heapq.heappush(queue, (new_cost, neighbor, path + [neighbor]))
# Define the map graph
map_graph = {
    'A': {'B': 1, 'D': 3},
    'B': {'A': 1, 'C': 2, 'E': 1},
    'C': {'B': 2, 'F': 1},
    'D': {'A': 3, 'E': 2},
    'E': {'B': 1, 'D': 2, 'F': 1},
    'F': {'C': 1, 'E': 1}
}
# Find the shortest path from A to F using A* search
shortest_path_A_to_F_astar = astar_shortest_path(map_graph, 'A', 'F')
print("Shortest path from A to F (A* search):", shortest_path_A_to_F_astar)
