class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        one = 1
        two = 2

        for i in range(n-2):
            temp = two
            two = one + two
            one = temp
        return two
