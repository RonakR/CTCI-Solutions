def loop_detection_1(ll):
    appearances = {}
    current_node = ll.head
    circular_node = False

    while current_node is not None and circular_node is False:
        if current_node in appearances:
            circular_node = current_node
        else:
            appearances[current_node] = current_node

        current_node = current_node.next

    return circular_node