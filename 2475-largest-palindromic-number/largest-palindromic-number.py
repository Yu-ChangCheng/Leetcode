class Solution(object):
    def largestPalindromic(self, num):
        """
        :type num: str
        :rtype: str
        """
        c = Counter(num)
        left = ""
        mid = ""

        for n, count in sorted(c.items())[::-1]:
            curr_count = n * (count//2)
            if count % 2 == 0:
                left += curr_count
            else:
                left += curr_count
                mid = max(mid, n)
        if left: left = left.lstrip("0")
        res = left + mid + left[::-1]
        return  res or "0"

