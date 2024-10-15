# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #            1
        #           / \
        #          2   3 
        #             / \
        #             1   6
        #            /     \
        #            5       7
        #           /         \
        #          1           8

        # There might be the case that the longest path doesn't pass original root!!!! But in the child's node as a root
        self.diameter = 0

        def depth(node):
            if not node:
                return 0
                
            left_depth = depth(node.left) # calculate every left node as root
            right_depth  = depth(node.right) # calculate every right node as root
            curr_diameter = left_depth + right_depth # calculate current diameter
            self.diameter = max(self.diameter, curr_diameter) 

            return 1 + max(left_depth, right_depth) 
        
        depth(root)
        return self.diameter
