import sys
def validate_bst_1(root):
    return True if check_bst(root, -sys.maxint) else False

def check_bst(root, max_so_far):
    if root is None: return max_so_far

    max_so_far = check_bst(root.left, max_so_far)
    if root.data >= max_so_far: max_so_far = root.data
    else: return False
    max_so_far = check_bst(root.right, max_so_far)
    return max_so_far