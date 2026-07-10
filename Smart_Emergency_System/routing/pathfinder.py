import heapq


class PathFinder:

    @staticmethod
    def shortest_path(graph, start):

        distances = {}

        previous = {}

        for node in graph.nodes:
            distances[node] = float("inf")
            previous[node] = None

        distances[start] = 0

        pq = []

        heapq.heappush(pq, (0, start))

        while pq:

            current_distance, current_node = heapq.heappop(pq)

            if not graph.nodes[current_node].safe:
                continue

            for neighbour, weight in graph.adjacency[current_node]:

                if not graph.nodes[neighbour].safe:
                    continue

                distance = current_distance + weight

                if distance < distances[neighbour]:

                    distances[neighbour] = distance
                    previous[neighbour] = current_node

                    heapq.heappush(
                        pq,
                        (distance, neighbour)
                    )
        return distances, previous
    
    @staticmethod
    def nearest_exit(graph, distances):

        best_exit = None
        best_distance = float("inf")

        for node in graph.nodes.values():

            if node.type.lower() == "exit":

                if distances[node.id] < best_distance:

                    best_distance = distances[node.id]
                    best_exit = node.id

        return best_exit
    @staticmethod
    def get_path(previous, destination):

        path = []

        current = destination

        while current is not None:
            path.append(current)
            current = previous[current]

        path.reverse()

        return path
    @staticmethod
    def find_shelter(graph, distances):

        shelter = None
        max_distance = -1

        for node in graph.nodes.values():

            # Ignore unsafe nodes
            if not node.safe:
                continue

            # Ignore unreachable nodes
            if distances[node.id] == float("inf"):
                continue

            # Ignore exits
            if node.type.lower() == "exit":
                continue

            # Choose the farthest reachable safe node
            if distances[node.id] > max_distance:
                max_distance = distances[node.id]
                shelter = node.id

        return shelter
