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
        while True:
            retString += str(currentNode.data) + " "
            currentNode = currentNode.next
            if currentNode is None: break

        return retString