class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data) + ": [" + str(self.left) + " " + str(self.right) + "] ,"


# root = TreeNode(8)
# left = TreeNode(7)
# root.left = left
# right = TreeNode(9)
# root.right = right
#
# print root