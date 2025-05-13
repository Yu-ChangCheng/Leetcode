class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        maxLength = 0
        seen = set()
        l = 0
        r = 0

        while l <= r and r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                maxLength = max(maxLength, r - l + 1)
                r += 1
            else:
                seen.remove(s[l])
                l += 1
        return maxLength