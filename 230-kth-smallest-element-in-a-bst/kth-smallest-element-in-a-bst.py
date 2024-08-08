# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # DFS, In-order(Left, Root, Right), recursive call
        self.k = k
        self.res = None
        self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return
        self.helper(node.left) # traverse left first and when popback return the value
        self.k -= 1 # traverse root
        if self.k == 0: 
            self.res = node.val 
            return
        self.helper(node.right) # traverse right



        # # Traverse the tree In-order
        # if not root:
        #     return None
        # stack = []
        # stack.append(root)
        
        # while stack:
        #     while root:
        #         stack.append(root)
        #         root = root.left

        #     root = stack.pop()
        #     k -= 1
        #     if k == 0:
        #         return root.val
        #     root = root.right

