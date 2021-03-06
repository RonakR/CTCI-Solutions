from utilities.linked_list import create_linked_list, get_random_node
from delete_middle_1 import delete_middle_1

def main():
    items_1 = create_linked_list([1,2,4,5,3,4,1,1,5,5,6])
    items_2 = create_linked_list(["alligator", "aardvark", "zebra", "zebra", "aardvark"])

    input_1 = get_random_node(items_1)
    input_2 = get_random_node(items_2)

    print "Solution 1: Replace contents of node with contents from the next node in the list."
    print "input: {input}, output: {output}".format(input=input_1,output=not delete_middle_1(input_1) or items_1)
    print "input: {input}, output: {output}\n".format(input=input_2,output=not delete_middle_1(input_2) or items_2)

if __name__ == '__main__':
    main()