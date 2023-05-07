class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list) # create list to use 26 bit counts as key and desired values as value
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1 # map char a to 0
            res[tuple(count)].append(s) # use tuple to so it can be used as a key
        return res.values() # return the values not the keys
