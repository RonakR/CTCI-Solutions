from is_unique_1 import is_unique_1
from is_unique_2 import is_unique_2

def main():
    print "input: '', output: {output}".format(output=is_unique_1(""))
    print "input: 1234, output: {output}".format(output=is_unique_1(1234))
    print "input: 'TestString', output: {output}".format(output=is_unique_1("TestString"))
    print "input: 'abcdefgb', output: {output}".format(output=is_unique_1("abcdefgh"))

    print "input: '', output: {output}".format(output=is_unique_2(""))
    print "input: 1234, output: {output}".format(output=is_unique_1(1234))
    print "input: 'TestString', output: {output}".format(output=is_unique_2("TestString"))
    print "input: 'abcdefgb', output: {output}".format(output=is_unique_2("abcdefgh"))

if __name__ == '__main__':
    main()