class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0 :
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    
        return res

