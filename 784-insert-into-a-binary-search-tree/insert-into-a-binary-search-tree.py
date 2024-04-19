# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)

        curr = root 
        while True:
            if curr.val > val:  # 4 > 5 (x) / 7 > 5 yes
                if not curr.left: #         / yes
                    curr.left = TreeNode(val) # / insert 5 
                    break
                curr = curr.left
            else:
                if not curr.right: # (x)
                    curr.right = TreeNode(val)
                    break
                curr = curr.right # curr = 7
        return root
             

        