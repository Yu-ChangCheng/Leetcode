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
            return None

        q = collections.deque()
        q.append(root)

        result = []

        # start BFS
        while q:
            level = []
            for i in range(len(q)): # to know how many nodes in current level
                curr_node = q.popleft()
                level.append(curr_node.val)
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            result.append(level[:])

        return result


                


        
