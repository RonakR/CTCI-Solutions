from utilities.linked_list import create_linked_list
import random

def main():
    items_1 = create_linked_list([1,2,4,5,3,4,1,1,5,5,6])
    items_2 = create_linked_list(["alligator", "aardvark", "zebra", "zebra", "aardvark"])

    # print "Solution 1: Replace contents of node with contents from the next node in the list."
    # print "input: {input}, output: {output}".format(input=input_1,output=not delete_middle_1(input_1) or items_1)
    # print "input: {input}, output: {output}\n".format(input=input_2,output=not delete_middle_1(input_2) or items_2)

def get_random_node(head):
    index = random.randint(1, len(head)-1)
    current_node = head
    for i in range(index):
        current_node = current_node.next

    return current_node

if __name__ == '__main__':
    main()