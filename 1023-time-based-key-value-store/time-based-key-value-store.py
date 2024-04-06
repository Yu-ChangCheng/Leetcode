class TimeMap(object):

    def __init__(self):
        self.hashmap = defaultdict(list) # [key1:[[value1, timestamp1],[value2, timestamp2]], key2: [value, timestamp]]

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.hashmap[key].append([value,timestamp])
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        values = self.hashmap[key]
        l = 0
        r = len(values) - 1
        s = ""

        while l <= r:
            m = (l + r) // 2
            if values[m][1] == timestamp:
                return values[m][0]
            if values[m][1] <= timestamp:
                s = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return s


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)