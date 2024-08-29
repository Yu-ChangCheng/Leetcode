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
        #         /\   /\
        #       4   5  1  6
        #                  \
        #                   7
        self.diameter = 0

        def depth(node):
            if not node:
                return 0
            
            left_depth = depth(node.left)
            right_depth  = depth(node.right)
            curr_diameter = left_depth + right_depth
            self.diameter = max(self.diameter, curr_diameter)
            return 1 + max(left_depth, right_depth) 
        
        depth(root)
        return self.diameter