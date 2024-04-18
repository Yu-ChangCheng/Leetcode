class MyHashMap(object):

    def __init__(self):
        self.map = [None] * 1000001

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.map[key] = value

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        val = self.map[key]
        return val if val != None else -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.map[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)