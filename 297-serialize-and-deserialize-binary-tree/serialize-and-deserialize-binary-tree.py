# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # 
        result = []
        def dfs(node):
            if not node:
                result.append("None")
                return
            result.append(str(node.val)) # Preorder-traverse root, left, right
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return " ".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(" ")
        queue = deque(data)

        def helper(queue): # Use queue to pop the root
            node = queue.popleft()
            if node == "None":
                return 
            root = TreeNode(int(node))
            root.left = helper(queue)
            root.right = helper(queue)
            return root
        return helper(queue)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))