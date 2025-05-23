class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
                
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1 
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < len(nums) - 1:
                        l += 1
        return res
