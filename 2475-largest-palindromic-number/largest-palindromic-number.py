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
            curr_num = n * (count//2)
            if count % 2 != 0 and mid == "":
                mid = n
            left += curr_num

        if left: left = left.lstrip('0')
        res = left + mid + left[::-1]
        return res or "0"



