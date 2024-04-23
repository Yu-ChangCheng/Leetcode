class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.res = 0

        def palindrom_count(left, right):
            while left >=0 and right < len(s) and s[left] == s[right]:
                self.res += 1
                left -= 1
                right += 1


        for i in range(len(s)):
            palindrom_count(i, i )
            palindrom_count(i, i + 1)
        return self.res

