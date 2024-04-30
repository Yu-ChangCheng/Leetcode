class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0: return 0
        if len(s) == 1: return 1

        l = 0
        substring_set = set()
        res = 0

        for r in range(len(s)):
            while s[r] in substring_set:
                substring_set.remove(s[l])
                l += 1
            substring_set.add(s[r])
            res = max(res, r-l+1)
        return res
        