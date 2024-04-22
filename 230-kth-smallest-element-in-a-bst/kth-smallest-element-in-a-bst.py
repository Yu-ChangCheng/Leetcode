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
        stack = []
        while stack or root:
            # Traverse to the leftest node
            while root:
                stack.append(root)
                root = root.left
            # pop one and decrease k by 1
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            # go to the right
            root = root.right
            

    #     self.k = k
    #     self.res = None
    #     self.helper(root)
    #     return self.res

    # # if doing recusively, make sure no use while loop, and base case is not node
    # # has to go to the left 
    # def helper(self, node): 
    #     if not node: 
    #         return
    #     self.helper(node.left)
    #     self.k -= 1
    #     if self.k == 0:
    #         self.res = node.val
    #         return
    #     self.helper(node.right)


    ''' Iterative
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right
    '''            