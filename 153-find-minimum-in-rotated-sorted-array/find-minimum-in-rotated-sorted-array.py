class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 5000
        l = 0 
        r = len(nums) - 1

        while l <= r:
            if nums[r] > nums[l]:
                res = min(res, nums[l])
                break
            
            m = (l+r) // 2
            res = min(nums[m], res)
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return res
                
            