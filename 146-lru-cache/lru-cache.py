class ListNode:
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
        self.hashmap = {}
        self.cap = capacity
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hashmap:
            self.remove_from_head(self.hashmap[key])
            self.insert_to_tail(self.hashmap[key])
            return self.hashmap[key].val
        return -1

    def remove_from_head(self, node):
        node_prev = node.prev
        node_next = node.next
        node_prev.next = node.next
        node_next.prev = node_prev
    
    def insert_to_tail(self, node):
        dummy = self.tail.prev
        dummy.next = node
        node.next = self.tail
        node.prev = dummy
        self.tail.prev = node
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        newNode = ListNode(key, value)
        if key in self.hashmap:
            oldNode = self.hashmap[key] 
            self.remove_from_head(oldNode)
            del oldNode

        self.hashmap[key] = newNode
        self.insert_to_tail(newNode)

        if len(self.hashmap) > self.cap:
            LRU = self.head.next
            self.remove_from_head(LRU)
            del self.hashmap[LRU.key]


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)