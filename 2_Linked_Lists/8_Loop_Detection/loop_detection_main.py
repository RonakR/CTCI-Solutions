import random
from utilities.linked_list import create_linked_list
from loop_detection_1 import loop_detection_1

def main():
    items_1 = create_linked_list([1,2,4,5,3,4,1,1,5,5,6])
    items_1.append_full_node(get_random_node(items_1))

    print "Solution 1: Run through both lists, compare where nodes start being similar."
    print "input: {input}, output: {output}".format(input=items_1,output=loop_detection_1(items_1).data)


def get_random_node(head):
    index = random.randint(1, len(head)-1)
    current_node = head
    for i in range(index):
        current_node = current_node.next

    return current_node

if __name__ == '__main__':
    main()