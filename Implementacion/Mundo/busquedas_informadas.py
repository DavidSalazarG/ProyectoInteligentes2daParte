import heapq

def a_star(graph, start, destination):
    priority_queue = [(0, start, [])]
    visited = set()
    visited_nodes = []

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node not in visited:
            path = path + [node]
            visited_nodes.append(node)

            if node == destination:
                return visited_nodes

            visited.add(node)

            for neighbor, weight in graph[node].items():
                heuristic_cost = heuristic(neighbor, destination)
                total_cost = cost + weight + heuristic_cost

                heapq.heappush(priority_queue, (total_cost, neighbor, path))

    return f"No se encontró una ruta por A* desde {start} a {destination}"


#Ejemplo heuristica
def heuristic(node, destination):
    x1, y1 = node
    x2, y2 = destination
    heuristica = abs(x1 - x2) + abs(y1 - y2)
    return heuristica