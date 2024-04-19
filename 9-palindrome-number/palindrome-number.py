class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False

        x_copy = x
        res = 0
        while x_copy:
            res = res * 10 + x_copy % 10
            x_copy = x_copy // 10

        return res == x

