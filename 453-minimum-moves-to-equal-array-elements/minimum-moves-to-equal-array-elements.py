class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sum of all elements in the final array is going to be k * e. 
        # On each move, the sum of the original array is going to increase by k - 1. 
        # So after m moves, the sum will increase by m(k - 1). So,
        # sum + m(k - 1) = k * e ---- equation (i)

        # In this equation, e is the only unknown other than m. How can we find e? 
        # Whatever the smallest integer is in nums, plus the number of moves m, will be equal to e. 
        # This is because with each m, we only increment the value by 1. So,
        # min + m = e ---- equation (ii)
        # sum + m * k - m = k * min + k * m (i + ii)
        # sum - m = k * min
        # m = sum - k * min
        return sum(nums) - (len(nums) * min(nums))