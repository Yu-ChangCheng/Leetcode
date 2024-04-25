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
        
        curr = leaf
        prev = None

        while curr:
            if curr.right == prev:
                if curr == root:
                    curr.right = None
                    curr.parent = prev
                    break
                elif curr.left:
                    curr.right = curr.left
            curr.left = curr.parent
            curr.parent = prev
            prev = curr
            curr = curr.left
        return leaf
