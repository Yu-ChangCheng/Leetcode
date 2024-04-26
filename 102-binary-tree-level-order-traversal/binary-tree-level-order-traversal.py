# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        q = deque()
        q.append(root)
        res = []

        while q: #3    
            level = [] # []
            for i in range(len(q)):
                node = q.popleft() #3
                if node: # true
                    level.append(node.val) # level = [3]
                    if node.left:
                        q.append(node.left) # q = [9]
                    if node.right:
                        q.append(node.right) # q = [9, 20]
            if level:
                res.append(level) # res = [[3]]
        return res
                