class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        for left in range(len(nums)-2):
            if left > 0 and nums[left] == nums[left - 1]: # make sure it is greater than 0 and make sure no duplicates on left
                continue
            mid = left + 1
            right = len(nums) - 1
            while mid < right:
                threeSum = nums[left] + nums[mid] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    mid += 1
                else:
                    res.append([nums[left], nums[mid], nums[right]])
                    while mid < right and nums[mid] == nums[mid + 1]:
                        mid += 1
                    while mid < right and nums[right] == nums[right - 1]:
                        right -= 1
                    mid += 1
                    right -= 1
        return res
