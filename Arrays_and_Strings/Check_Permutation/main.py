from check_permutation_1 import check_permutation_1
from check_permutation_2 import check_permutation_2

def main():
    print "Solution 1: Run through first string and check if in second string"
    print "input: '', '' , output: {output}".format(output=check_permutation_1("", ""))
    print "input: 'sales', 'lases', output: {output}".format(output=check_permutation_1("sales", "lases"))
    print "input: 'trees', 'treed', output: {output}\n".format(output=check_permutation_1("trees", "treed"))

    print "Solution 2: Map contents for first string to hash table, compare second string to hash table"
    print "input: '', '' , output: {output}".format(output=check_permutation_2("", ""))
    print "input: 'sales', 'lases', output: {output}".format(output=check_permutation_2("sales", "lases"))
    print "input: 'trees', 'treed', output: {output}".format(output=check_permutation_2("trees", "treed"))

if __name__ == '__main__':
    main()