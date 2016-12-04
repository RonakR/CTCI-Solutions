from utilities.linked_list import create_linked_list
from remove_dups_1 import remove_dups_1
from remove_dups_2 import remove_dups_2

def main():
    items_1 = create_linked_list([1,2,4,5,3,4,1,1,5,5,6])
    items_2 = create_linked_list(["alligator", "aardvark", "zebra", "zebra", "aardvark"])

    print "Solution 1: Run through list adding and comparing to a dictionary"
    print "input: [1,2,4,5,3,4,1,5,5,6], output: {output}".format(output=remove_dups_1(items_1))
    print "input: ['alligator', 'aardvark', 'zebra', 'zebra', 'aardvark'], output: {output}\n".format(output=remove_dups_1(items_2))

    print "Solution 2: For each character, use a runner to run through the rest of the list"
    print "input: [1,2,4,5,3,4,1,5,5,6], output: {output}".format(output=remove_dups_2(items_1))
    print "input: ['alligator', 'aardvark', 'zebra', 'zebra', 'aardvark'], output: {output}\n".format(output=remove_dups_2(items_2))


if __name__ == '__main__':
    main()