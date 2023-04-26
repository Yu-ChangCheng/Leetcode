class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen={}

        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining],i]
            seen[v] = i
        return []
            
print(Solution().twoSum(nums=[2,7,11,15], target=9))
print(Solution().twoSum(nums=[3,3], target=6))
print(Solution().twoSum(nums=[3,2,4], target=6))


