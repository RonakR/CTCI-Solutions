from utilities.tree_node import TreeNode
from validate_bst_1 import validate_bst_1

def main():
    valid_bst_root = create_valid_bst()
    invalid_bst_root = create_invalid_bst()

    print "Solution 1: In Order search through tree, compare to max_so_far"
    print "input: 8:[7:[6:[None None],7:[None None]],10:[9:[None None],15:[None None]]], output: {output}"\
        .format(output=validate_bst_1(valid_bst_root))
    print "input: 8:[7:[6:[None None],9:[None None]],10:[None 15:[None None]]], output: {output}"\
        .format(output=validate_bst_1(invalid_bst_root))

def create_valid_bst():
    six = TreeNode(6, None, None)
    sevenDupe = TreeNode(7)
    seven = TreeNode(7, six, sevenDupe)
    nine = TreeNode(9, None, None)
    fifteen = TreeNode(15, None, None)
    ten = TreeNode(10, nine, fifteen)
    eight = TreeNode(8, seven, ten) ##root

    return eight

def create_invalid_bst():
    six = TreeNode(6, None, None)
    nine = TreeNode(9, None, None)
    seven = TreeNode(7, six, nine)
    fifteen = TreeNode(15, None, None)
    ten = TreeNode(10, None, fifteen)
    eight = TreeNode(8, seven, ten) ##root

    return eight

if __name__ == '__main__':
    main()