class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, data):
        nextNode = Node(data)
        currentNode = self

        while (currentNode.next is not None):
            currentNode = currentNode.next

        currentNode.next = nextNode

    def __str__(self):
        currentNode = self
        retString = ""
        while (currentNode.next is not None):
            retString += currentNode.data + " "
            currentNode = currentNode.next

        return retString