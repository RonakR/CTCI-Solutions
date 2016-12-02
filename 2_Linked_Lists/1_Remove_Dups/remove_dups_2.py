def remove_dups_2(head):
    current_node = head
    runner_node = head

    while current_node is not None:
        while runner_node.next is not None:
            if current_node.data == runner_node.next.data:
                runner_node.next = runner_node.next.next
            else:
                runner_node = runner_node.next
        current_node = current_node.next
        runner_node = current_node

    return head


