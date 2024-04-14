class Node():
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.hashmap = {}
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        p_prev = node.prev
        p_next = node.next
        p_prev.next = p_next
        p_next.prev = p_prev

    def insert(self, node):
        p_prev = self.tail.prev
        p_next = self.tail
        p_prev.next = node
        p_next.prev = node
        node.next = p_next
        node.prev = p_prev
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].val
        return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        new_node = Node(key,value)
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            del self.hashmap[key]
        self.hashmap[key] = new_node
        self.insert(new_node)

        if len(self.hashmap) > self.capacity:
            lru_node = self.head.next
            del self.hashmap[lru_node.key]
            self.remove(lru_node)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)