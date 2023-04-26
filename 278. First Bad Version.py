# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n

        while left < right:
            guess = int((left + right) / 2)
            if isBadVersion(guess):
                right = guess
            else:
                left = guess + 1

        return left
