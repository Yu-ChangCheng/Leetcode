"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def flipBinaryTree(self, root, leaf):
        """
        :type node: Node
        :rtype: Node
        """
        # Node.__str__ = lambda cur: ('Node: (' +
        #     (f'left={cur.left.val}' if cur and cur.left else 'left=None') +
        #     (f' right={cur.right.val}' if cur and cur.right else ' right=None') +
        #     (f' parent={cur.parent.val}' if cur and cur.parent else ' parent=None') +
        #     ')'
        #    )
        
        # From leaf to root, for each node
        # moves left subtree to right if it exists
        # makes parent node become its left child
        # updates node.parent and breaks the pointer in its parent node to itself
        # Time Complexity O(H) H: the depth from root to leaf
        node, parent = leaf, None
        while node != root:
            if node.left:
                node.right = node.left
                
            node.left, node.parent = node.parent, parent
            parent, node = node, node.left
            
            if node.left == parent:
                node.left = None
            else:
                node.right = None
        
        root.parent = parent
        return leaf
