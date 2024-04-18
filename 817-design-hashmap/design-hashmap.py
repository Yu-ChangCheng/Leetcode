class ListNode:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap(object):

    def __init__(self):
        self.map = [ListNode() for i in range(1000)]

    def hash(self, key):
        return key % len(self.map)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        cur = self.map[self.hash(key)] # reach to the dummy node
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        cur = self.map[self.hash(key)]
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        cur = self.map[self.hash(key)]
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return 
            cur = cur.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)