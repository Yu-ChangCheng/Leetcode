# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        '''
        res = 0
        maxVal = root.val
        q = deque([[root, maxVal]]) # storage the maxVal so far
        first_node = False

        while q:
            node, maxVal = q.popleft()
            if node.val >= maxVal:  
                res += 1

            if node.left:
                q.append([node.left, max(maxVal, node.val)])
            if node.right:    
                q.append([node.right, max(maxVal, node.val)])

                    
        return res
        '''
        self.res = 0

        def dfs(node, maxVal):
            if not node:
                return
            if node.val >= maxVal:
                self.res += 1

            dfs(node.left, max(node.val, maxVal))
            dfs(node.right, max(node.val, maxVal))
            return
        dfs(root,root.val)
        return self.res
        
