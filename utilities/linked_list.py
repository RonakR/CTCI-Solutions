class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __len__(self):
        length = 0
        current_node = self

        while current_node is not None:
            length+=1
            current_node = current_node.next

        return length

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