"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        queue = deque()
        queue.append(node) # queue will store all the original node
        lookup = {}
        lookup[node] = Node(node.val, []) # loop up will store all the copied node

        while queue:
            curr_node = queue.popleft()
            for neighbor in curr_node.neighbors:
                if neighbor not in lookup: # if not exist in the map
                    lookup[neighbor] = Node(neighbor.val, []) # create a copy
                    queue.append(neighbor) # add it to the queue for future
                lookup[curr_node].neighbors.append(lookup[neighbor]) # append neighbor node to curr_node's neighbor list
        return lookup[node] # when queue is empty return the first copy node 
                
                
