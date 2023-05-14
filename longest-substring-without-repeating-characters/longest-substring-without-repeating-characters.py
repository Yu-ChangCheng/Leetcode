class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        'abcbc'
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] not in charSet:
                charSet.add(s[r])
                res = max(res, r-l+1)
            else:
                while l < r and s[l] != s[r]:
                    charSet.remove(s[l])
                    l += 1
                l += 1
        return res
