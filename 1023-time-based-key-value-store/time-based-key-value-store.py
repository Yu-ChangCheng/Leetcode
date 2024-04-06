class TimeMap(object):

    def __init__(self):
        self.hashmap = defaultdict(list)
        
    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.hashmap[key].append([value, timestamp])

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        values = self.hashmap[key]
        l = 0 
        r = len(values) - 1
        res = ''

        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                l = m + 1
                res = values[m][0]
            else:
                r = m - 1
        return res




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)