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
        node = root
        if not node:
            return TreeNode(val = val)
            
        while node:
            if node.val > val:
                if not node.left:
                    node.left = TreeNode(val = val)
                    break
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = TreeNode(val = val)
                    break
                else:
                    node = node.right

        return root
        
            