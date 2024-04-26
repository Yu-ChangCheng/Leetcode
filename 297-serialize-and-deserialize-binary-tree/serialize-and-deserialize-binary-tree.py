# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        node_list = []
        def dfs(node):
            if not node:
                node_list.append("None")
                return
            node_list.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        
        return " ".join(node_list)
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        node_list = data.split(" ")
        queue = deque(node_list)

        def helper(queue):
            node = queue.popleft()
            if node == "None":
                return
            root = TreeNode(node)
            root.left = helper(queue)
            root.right = helper(queue)
            return root
        return helper(queue)    

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))