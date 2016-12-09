from utilities.node import Node

class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, item):
        newItem = Node(item)
        if self.first is None:
            self.first = newItem
            self.last = self.first
        else:
            self.last.next = newItem
            self.last = newItem

    def remove(self):
        if self.first is None: raise IndexError("Empty Queue")
        data = self.first.data
        self.first = self.first.next
        if self.first is None:
            self.last = None

        return data

    def peek(self):
        if self.first is None: raise IndexError("Empty Queue")
        return self.first.data

    def isEmpty(self):
        return self.first == None

    def __str__(self):
        current_node = self.first
        retString = ""
        while current_node is not None:
            retString += str(current_node.data) + " "
            current_node = current_node.next

        return retString