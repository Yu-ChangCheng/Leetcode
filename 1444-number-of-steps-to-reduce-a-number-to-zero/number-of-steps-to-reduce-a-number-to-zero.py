class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        ct = 0
        while num != 0:
            num = num / 2 if num % 2 == 0 else num - 1
            ct += 1
        return ct