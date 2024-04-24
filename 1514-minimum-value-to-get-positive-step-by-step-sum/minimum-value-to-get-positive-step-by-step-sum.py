class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        start_value = 1

        for n in nums[::-1]:
            if start_value - n < 1: 
                start_value = 1
            else:  
                start_value += -n
        return start_value
        '''
        prefix_sum = 0
        min_start_value = 0

        for num in nums:
            prefix_sum += num
            min_start_value = min(min_start_value, prefix_sum)
        return -min_start_value + 1
        