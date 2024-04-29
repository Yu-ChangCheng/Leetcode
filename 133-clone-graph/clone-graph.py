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
        # check if not node return None
        if not node:
            return None

        # have a hashmap and queue to clone graph BFS
        visited = {}
        queue = deque([node]) # deque items has to iterable otherwise use append, Note: this node contains neighbors
        visited[node] = Node(node.val, []) # initailize the first node as copy and neighbor as an empty list

        while queue:
            visited_node = queue.popleft() # pop out the node from queue
            for neighbor in visited_node.neighbors: # check the neighbor in the node's neighbors Note the neighbor here is also a Node already
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visited[visited_node].neighbors.append(visited[neighbor])
        return visited[node]
                
