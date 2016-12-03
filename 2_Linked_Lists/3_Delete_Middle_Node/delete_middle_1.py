from utilities.linked_list import Node
def delete_middle_1(node):
    if node is None or node.next is None:
        return False

    new_node = node.next
    node.data = new_node.data
    node.next = new_node.next
    return True