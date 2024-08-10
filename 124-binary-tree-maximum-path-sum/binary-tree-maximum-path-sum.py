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

            # if child node is negative, don't include this by compare to 0
            left = max(0, postorder(node.left)) # left 
            right = max(0, postorder(node.right)) # right
            currSum = node.val + left + right # node
            self.maxLength = max(self.maxLength, currSum)
            return node.val + max(left, right)

        postorder(root)
        return self.maxLength

        # O(N)
        # O(H), O(logN) if is balanced tree