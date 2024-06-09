# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        

        def dfs(node):
            if not node:
                return [True, 0]
            
            left = dfs(node.left)
            right = dfs(node.right)

            isBlanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [isBlanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]


    def dfs(self, node):
        if not node:
            return [True, 0] # [True, level]

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        isBlanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

        return [isBlanced, 1 + max(left[1], right[1])]

        return self.dfs(root)[0]