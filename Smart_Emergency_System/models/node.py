class Node:
    def __init__(self, node_id, node_type, x, y, floor):
        self.id = node_id
        self.type = node_type
        self.x = x
        self.y = y
        self.floor = floor
        self.safe = True
        self.visited = False

    def __str__(self):
        status = "Safe" if self.safe else "Unsafe"
        return f"{self.id} ({self.type}) Floor:{self.floor} ({self.x},{self.y}) - {status}"