class HazardManager:

    @staticmethod
    def apply_fire(graph, fire_node_id):

        if fire_node_id not in graph.nodes:
            print("Fire location not found!")
            return

        # Mark only the fire node unsafe
        graph.nodes[fire_node_id].safe = False

        # Disable all lifts
        for node in graph.nodes.values():
            if node.type.lower() == "lift":
                node.safe = False

        print(f"\nFire detected at {fire_node_id}")
        print("Fire node blocked.")
        print("All lifts disabled.")