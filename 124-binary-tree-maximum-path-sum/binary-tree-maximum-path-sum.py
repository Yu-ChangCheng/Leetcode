# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
            
        self.maxLength = -float('Inf')

        def postorder(node):
            if not node:
                return
            
            left = max(0, postorder(node.left))
            right = max(0, postorder(node.right))
            currSum = node.val + left + right
            self.maxLength = max(self.maxLength, currSum)
            return node.val + max(left, right)
        postorder(root)
        return self.maxLength