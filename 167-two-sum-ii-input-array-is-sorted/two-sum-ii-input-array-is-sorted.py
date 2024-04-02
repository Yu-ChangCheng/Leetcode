class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers) - 1

        twosum = 0 
        while l < r:
            twosum = numbers[l] + numbers[r]
            if twosum > target:
                r -= 1
            elif twosum < target:
                l += 1
            else:
                return [l+1, r+1]
