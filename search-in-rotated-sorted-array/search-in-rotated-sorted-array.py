class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l , r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]:  # left half is sorted
                if nums[l] <= target < nums[m]: # target is in the left half
                    r = m - 1
                else:  # target is in the right half
                    l = m + 1
            else:  # right half is sorted
                if nums[m] < target <= nums[r]: # target is in the right half
                    l = m + 1
                else:  # target is in the left half
                    r = m - 1

        return -1
