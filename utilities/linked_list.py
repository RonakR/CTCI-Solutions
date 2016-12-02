class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, data):
        next_node = Node(data)
        current_node = self

        while (current_node.next is not None):
            current_node = current_node.next

        current_node.next = next_node

    def __str__(self):
        current_node = self
        retString = ""
        while current_node is not None:
            retString += str(current_node.data) + " "
            current_node = current_node.next

        return retString