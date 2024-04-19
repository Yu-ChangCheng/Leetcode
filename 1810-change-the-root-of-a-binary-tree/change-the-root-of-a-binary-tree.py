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
        
        cur = leaf
        prev = None
        while cur:
            if cur.right == prev:
                if cur == root:
                    cur.right = None
                    cur.parent = prev
                    # print(cur)
                    break
                elif cur.left:
                    cur.right = cur.left
            cur.left = cur.parent
            cur.parent = prev
            prev = cur
            print(cur)
            cur = cur.left
        # print('')
        return leaf
            