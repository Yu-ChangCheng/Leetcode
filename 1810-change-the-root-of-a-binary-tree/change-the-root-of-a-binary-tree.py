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
        # Initialize `cur` to the leaf node which will become the new root
        cur = leaf
        # `prev` will keep track of the previous node processed in the loop, starts as None
        prev = None

        # Loop until `cur` is None, which means we've reached beyond the original root
        while cur:
            # If the current node's right child is the previous node, we adjust its right child
            if cur.right == prev:
                # If the current node is the original root, we need to finish processing
                if cur == root:
                    cur.right = None  # Disconnect the right child
                    cur.parent = prev  # Set its parent to the previous node (will be None if it's the leaf)
                    break
                # If the current node is not the root and has a left child,
                # move the left child to the right position to maintain tree structure
                elif cur.left:
                    cur.right = cur.left

            # The current node's left child should now point to its parent,
            # effectively reversing the parent-child relationship
            cur.left = cur.parent

            # Update the parent of the current node to be the previous node,
            # thus reversing the parent pointer direction
            cur.parent = prev

            # Move `prev` up to `cur`, preparing it to be the new parent in the next iteration
            prev = cur

            # Move to the next node in the path, which is the original parent of `cur`
            # Now `cur.left` is the new `cur` because we are tracing back the tree towards the original root
            cur = cur.left

        # Return the new root of the tree, which is the `leaf` node we started with
        return leaf
                