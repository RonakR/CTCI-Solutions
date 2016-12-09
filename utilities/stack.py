from utilities.node import Node

class Stack:
    def __init__(self):
        self.top = None

    def pop(self):
        if self.top is None: raise IndexError("Empty Stack")
        data = self.top.data
        self.top = self.top.next
        return data

    def push(self, item):
        newTop = Node(item)
        newTop.next = self.top
        self.top = newTop

    def peek(self):
        if self.top is None: raise IndexError("Empty Stack")
        return self.top.data

    def isEmpty(self):
        return self.top is None

    def __str__(self):
        current_node = self.top
        retString = ""
        while current_node is not None:
            retString += str(current_node.data) + " "
            current_node = current_node.next

        return retString