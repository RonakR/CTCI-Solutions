def remove_dups_1(ll):
    appearances = {}
    current_node = ll.head
    prev_node = None
    while current_node is not None:
        if current_node.data not in appearances:
            appearances[current_node.data] = current_node.data
            prev_node = current_node
        else:
            prev_node.next = current_node.next

        current_node = current_node.next

    return ll


