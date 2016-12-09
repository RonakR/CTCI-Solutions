import random
from utilities.node import Node

class LinkedList:
    def __init__(self, data, next=None):
        self.head = Node(data, next)

    def __len__(self):
        length = 0
        current_node = self.head

        while current_node is not None:
            length+=1
            current_node = current_node.next

        return length

    def __str__(self):
        max = 30
        current_node = self.head
        retString = ""
        while current_node is not None and max:
            retString += str(current_node.data) + " "
            current_node = current_node.next
            max-=1

        return retString

    def append(self, data):
        next_node = Node(data)
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = next_node

    def append_full_node(self, node):
        current_node = self.head

        while (current_node.next is not None):
            current_node = current_node.next

        current_node.next = node

def create_linked_list(items):
    if not items: return "Empty list."

    head = LinkedList(items[0])
    for item in items[1:]:
        head.append(item)

    return head

def get_random_node(ll):
    index = random.randint(1, len(ll)-1)
    current_node = ll.head
    for i in range(index):
        current_node = current_node.next

    return current_node