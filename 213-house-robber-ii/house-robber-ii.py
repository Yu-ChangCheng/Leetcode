class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return max(nums)
        
        # 
        nums1 = nums[:n-1]
        nums2 = nums[1:]

        if nums1[0] > nums[1]:
            nums1[1] = nums1[0]
        
        if nums2[0] > nums2[1]:
            nums2[1] = nums2[0]

        for i in range(2, n-1):
            nums1[i] = max(nums1[i-2]+nums1[i], nums1[i-1])
            nums2[i] = max(nums2[i-2]+nums2[i], nums2[i-1])
        
        return max(nums1[-1], nums2[-1])
