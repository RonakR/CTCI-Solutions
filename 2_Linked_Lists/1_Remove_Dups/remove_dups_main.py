from utilities.linked_list import Node
from remove_dups_1 import remove_dups_1

def main():
    soln_1_items_1 = [1,2,4,5,3,4,1,5,5,6]
    soln_1_items_2 = ["aligator", "aardvark", "zebra", "zebra", "aardvark"]

    print "Solution 1: Run through list adding and comparing to a dictionary"
    print "input: [1,2,4,5,3,4,1,5,5,6], output: {output}".format(output=remove_dups_1(createLinkedList(soln_1_items_1)))
    print "input: ['aligator', 'aardvark', 'zebra', 'zebra', 'aardvark'], output: {output}\n".format(output=remove_dups_1(createLinkedList(soln_1_items_2)))


def createLinkedList(items):
    if not items: return "Empty list."

    head = Node(items[0])
    for item in items[1:]:
        head.append(item)

    return head


if __name__ == '__main__':
    main()