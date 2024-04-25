class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.res = 0

        def isPalindrom(left, right, s):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                self.res += 1
                left -= 1
                right += 1
        
        for i in range(len(s)):
            isPalindrom(i, i, s)
            isPalindrom(i, i+1, s)
        return self.res