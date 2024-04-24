class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start_value = 1

        for n in nums[::-1]:
            if start_value - n < 1:
                start_value = 1
            else:  
                start_value += -n
        return start_value

        