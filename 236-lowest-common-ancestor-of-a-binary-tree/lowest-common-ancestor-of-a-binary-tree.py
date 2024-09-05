# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # base case if leaf is null just return
        # p = 8, q = 1
        node = root # 3
        if not node:
            return None
            
        if node == p or node == q: #if any root is p or q just return the value
            return node

        left_node = self.lowestCommonAncestor(node.left, p , q) # 5
        right_node = self.lowestCommonAncestor(node.right, p , q) # 1
        
        if (left_node and right_node): # 5, 1
            return node # return 3

        elif (not left_node and right_node):
            return right_node

        elif (not right_node and left_node):
            return left_node

        return None

