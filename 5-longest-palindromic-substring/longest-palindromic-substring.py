class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Also check out 647
        self.res = ""
        self.res_len = 0

        def isPalindrome(left, right):
            # if in bound and equal keep expanding the window
            while 0 <= left and right < len(s) and left <= right and s[left] == s[right]:
                if right - left + 1 > self.res_len:
                    self.res = s[left:right+1]
                    self.res_len = right - left + 1
                left -= 1
                right += 1

        # for each chars in the string TC: O(n^2) / SC: O(n)
        for i in range(len(s)):
            isPalindrome(i, i+1)
            isPalindrome(i, i)
        return self.res            