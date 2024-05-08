class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
 
        n = len(nums)
        if k > n:
            k %= n 
        first = nums[n-k:][:]
        second = nums[:n-k][:]
        ans = first + second
        for i in range(len(ans)):
            nums[i] = ans[i]
        