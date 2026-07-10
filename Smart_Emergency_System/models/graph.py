from models.edge import Edge


class Graph:

    def __init__(self):
        self.nodes = {}
        self.edges = []
        self.adjacency = {}

    def add_node(self, node):
        self.nodes[node.id] = node
        self.adjacency[node.id] = []

    def add_edge(self, node1_id, node2_id):

        node1 = self.nodes[node1_id]
        node2 = self.nodes[node2_id]

        edge = Edge(node1, node2)
        self.edges.append(edge)

        self.adjacency[node1_id].append((node2_id, edge.weight))
        self.adjacency[node2_id].append((node1_id, edge.weight))

    def display_summary(self):

        print("\n===== BUILDING SUMMARY =====")

        print(f"Total Nodes : {len(self.nodes)}")
        print(f"Total Edges : {len(self.edges)}")

        print("\nNodes")

        for node in self.nodes.values():
            print(node)

        print("\nEdges")

        for edge in self.edges:
            print(edge)