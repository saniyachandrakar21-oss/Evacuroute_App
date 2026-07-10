import json

from models.node import Node
from models.graph import Graph


class BuildingLoader:

    @staticmethod
    def load(filename):

        graph = Graph()

        with open(filename, "r") as file:
            data = json.load(file)

        # Load Nodes
        for node in data["nodes"]:

            new_node = Node(
                node["id"],
                node["type"],
                node["x"],
                node["y"],
                node["floor"]
            )

            graph.add_node(new_node)

        # Load Edges
        for edge in data["edges"]:

            graph.add_edge(
                edge["from"],
                edge["to"]
            )

        return graph