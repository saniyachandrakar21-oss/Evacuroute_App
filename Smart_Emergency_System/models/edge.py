import math


class Edge:

    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2

        dx = node1.x - node2.x
        dy = node1.y - node2.y
        df = node1.floor - node2.floor

        self.weight = math.sqrt(dx**2 + dy**2 + df**2)

    def __str__(self):
        return f"{self.node1.id} <--> {self.node2.id}  Distance={self.weight:.2f}"