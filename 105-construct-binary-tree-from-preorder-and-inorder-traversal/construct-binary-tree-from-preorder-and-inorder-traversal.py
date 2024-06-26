# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        dict_inorder = {}
        for ind, val in enumerate(inorder):
            dict_inorder[val] = ind

        if inorder:
            m_value = preorder.pop(0)
            INDEX = dict_inorder[m_value]
            root = TreeNode(m_value)
            root.left = self.buildTree(preorder, inorder[:INDEX])
            root.right = self.buildTree(preorder, inorder[INDEX+1:])
            return root
    