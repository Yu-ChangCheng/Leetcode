# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not q and not p:
            return True
        if (not q and p) or (not p and q) or (p.val != q.val):
            return False
        
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)
