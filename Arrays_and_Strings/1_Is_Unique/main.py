from is_unique_1 import is_unique_1
from is_unique_2 import is_unique_2
from is_unique_book import is_unique_book

def main():
    print "Solution 1: Put string in hash table with out any collisions"
    print "input: '', output: {output}".format(output=is_unique_1(""))
    print "input: 1234, output: {output}".format(output=is_unique_1(1234))
    print "input: 'TestString', output: {output}".format(output=is_unique_1("TestString"))
    print "input: 'abcdefgh', output: {output}\n".format(output=is_unique_1("abcdefgh"))

    print "Solution 2: Sort string, compare adjacent characters"
    print "input: '', output: {output}".format(output=is_unique_2(""))
    print "input: 1234, output: {output}".format(output=is_unique_1(1234))
    print "input: 'TestString', output: {output}".format(output=is_unique_2("TestString"))
    print "input: 'abcdefgh', output: {output}\n".format(output=is_unique_2("abcdefgh"))

    print "Solution 3: (From book) 128 length array of False, mark true at ASCII value of current char"
    print "input: '', output: {output}".format(output=is_unique_book(""))
    print "input: 1234, output: {output}".format(output=is_unique_book(1234))
    print "input: 'TestString', output: {output}".format(output=is_unique_book("TestString"))
    print "input: 'abcdefgh', output: {output}".format(output=is_unique_book("abcdefgh"))

if __name__ == '__main__':
    main()