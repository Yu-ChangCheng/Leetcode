class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # [4,5,6,7,0,1,2] left rotated list (nums[l] <= nums[m])
        #. l    ,m,    r                    (nums[l] <= t1 <= nums[m]) we shift or r = m - 1
        #.   t1.     t2                     l += 1
 
        # [4,5,6,0,1,2,3] right rotated list nums[l] > nums[m]
        #. l    ,m,    r                    (nums[m] <= t2 <= nums[r]) we shift or l = m + 1
        #.   t1.     t2                     r -= 1

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[l] <= nums[m]: # left rotated list
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else: # right rotated list
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
            

