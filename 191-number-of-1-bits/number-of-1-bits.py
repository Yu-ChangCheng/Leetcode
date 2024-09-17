class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n:
            ans += n % 2
            n = n >> 1
        return ans

        # return bin(n).count('1')


        # res = 0
        # while n:
        #     n = n & (n-1)
        #     res += 1
        # return res
