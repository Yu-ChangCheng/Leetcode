class Node():
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.cap = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # head (P) -> node <- tail
    def remove(self, node):
        p = node.prev
        p.next = node.next
        node.next.prev = p
    
    # head (P) -> node -> tail
    def insert(self, node):
        p = self.tail.prev
        p.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = p

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
        if key in self.cache: # shift our node to right (tail)
            self.remove(self.cache[key])
            del self.cache[key]
        elif len(self.cache) == self.cap: # evict the node next to head
            n = self.head.next
            self.remove(n) # delete the node
            del self.cache[n.key] # delete from the dict
        
        n = Node(key, value) # put the node to the prev before tail
        self.cache[key] = n
        self.insert(n)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)