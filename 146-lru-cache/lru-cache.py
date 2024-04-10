class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = {} # map kep to node
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def insert(self, node):
        p = self.tail.prev
        p.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = p

    def remove(self, node):
        p = node.prev
        p.next = node.next
        node.next.prev = p

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        n = self.cache[key]
        self.remove(n)
        self.insert(n)
        return n.val
      

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]
        elif len(self.cache) == self.cap:
            n = self.head.next
            self.remove(n)
            del self.cache[n.key]
        
        n = Node(key, value)
        self.cache[key] = n
        self.insert(n)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)