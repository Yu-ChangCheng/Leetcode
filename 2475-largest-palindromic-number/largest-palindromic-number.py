class Solution(object):
    def largestPalindromic(self, num):
        """
        :type num: str
        :rtype: str
        """
        c = Counter(num)
        left = ""
        mid = ""

        for n in sorted(c)[::-1]:
            cur = n * (c[n]//2)
            if c[n] % 2 ==0:
                left += cur
            else:
                left += cur
                mid = max(mid,n)
        
        if left: left = left.lstrip('0')
        return (left + mid + left[::-1]) or '0'