class GraphNode:
    def __init__(self, data, children=None):
        self.data = data
        self.children = children

    def __str__(self):
        return self.data + ": " + str(self.children)