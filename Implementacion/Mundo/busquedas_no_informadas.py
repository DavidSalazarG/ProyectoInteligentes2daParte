import heapq
from collections import deque
from itertools import count

#Recorrido en profundidad
def bfs(graph, start, destination):
    #print(start,destination)
    adyacencias = {}
    #print("grafo para bfs: ", graph)
    visited = set()
    completo = []
    queue = deque([(start, [])])

    if start == destination:
        return f"El nodo de inicio es igual al nodo de destino: {start}"

    while queue:
        node, path = queue.popleft()

        if node not in visited:
            path = path + [node]
            completo.append(node)

            if node == destination:
     #           print("solucion bfs: ",completo)
      #          print("camino: ", path)
       #         print("la solución está en el nivel :", len(path) - 1)
                return completo

            visited.add(node)


            neighbors = graph[node]
            for neighbor, weight in neighbors.items():
        #        print("vecinos: ", neighbors)
                if neighbor not in visited:
                    new_path = list(path)
                    queue.append((neighbor, new_path))

    return f"No se encontró un recorrido en anchura desde {start} a {destination}"
def bfs_sustentacion(graph, start, destination):
    print(start,destination)
    print("grafo para bfs: ", graph)
    visited = set()
    completo = []
    queue = deque([(start, [])])

    if start == destination:
        return f"El nodo de inicio es igual al nodo de destino: {start}"

    while queue:
        node, path = queue.popleft()

        if node not in visited:
            path = path + [node]
            completo.append(node)

            if node == destination:

                return completo

            visited.add(node)


            neighbors = graph[node]
            for neighbor, weight in neighbors.items():
                if neighbor not in visited:
                    new_path = list(path)
                    queue.append((neighbor, new_path))

    return f"No se encontró un recorrido en anchura desde {start} a {destination}"

def dfs(graph, start, destination):
    visited = set()
    visited_nodes = []  # Lista para almacenar nodos visitados durante la búsqueda

    def dfs_recursive(node):
        visited.add(node)
        visited_nodes.append(node)

        if node == destination:
            return True  # Indicar que se encontró el destino y detener la expansión

        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                if dfs_recursive(neighbor):
                    return True  # Se encontró el destino, detener la expansión

    dfs_recursive(start)
    #print(visited_nodes)
    return visited_nodes

def uniform_cost_search(graph, start, destination):
    print(graph)
    priority_queue = [(0, start, [])]
    visited = set()
    completo = []
    orden = 50

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node not in visited:
            path = path + [node]
            completo.append(node)

            if node == destination:
                return completo

            visited.add(node)

            for neighbor, costo in graph[node].items():
                orden -= 0.1
                heapq.heappush(priority_queue, ((cost + costo)-orden, neighbor, path))


    return f"No se encontró un recorrido de costo uniforme desde {start} a {destination}"