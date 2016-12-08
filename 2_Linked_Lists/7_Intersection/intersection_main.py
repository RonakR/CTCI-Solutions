import random
from utilities.linked_list import create_linked_list
from intersection_1 import intersection_1

def main():
    items_1 = create_linked_list([1,2,4,5,3,4,1,1,5,5,6])
    items_2 = create_linked_list([12, 13, 14])


    print "Solution 1: Run through both lists, compare where nodes start being similar."
    print "input: {input_1}, {input_2}, output: {output}".format(input_1=items_1, input_2=items_2,output=intersection_1(items_1, items_2))
    items_2.next.next.next = items_1.next.next.next
    print "input: {input_1}, {input_2}, output: {output}".format(input_1=items_1, input_2=items_2,output=intersection_1(items_1, items_2))

if __name__ == '__main__':
    main()