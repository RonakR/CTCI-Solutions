from urlify_1 import urlify_1
from urlify_2 import urlify_2

def main():
    print "Solution 1: Strip, split on space, join with %20"
    # print "input: '', '' , output: {output}".format(output=urlify_1("", 0))
    print "input: 'Mr John Smith    ', 13, output: {output}".format(output=urlify_1("Mr John Smith    ", 13))
    print "input: 'Test   Test      ', 11, output: {output}\n".format(output=urlify_1("Test   Test      ", 11))

    print "Solution 2: Split everything, walk the list from the back and populate the list back to front"
    # print "input: '', '' , output: {output}".format(output=urlify_1("", 0))
    print "input: 'Mr John Smith    ', 13, output: {output}".format(output=urlify_2("Mr John Smith    ", 13))
    print "input: 'Test   Test      ', 11, output: {output}\n".format(output=urlify_2("Test   Test      ", 11))



if __name__ == '__main__':
    main()