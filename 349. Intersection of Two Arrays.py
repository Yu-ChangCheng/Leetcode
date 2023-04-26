"""
Time complexity : O(N+M) where O(N) for converting to set and O(M) for iterating over other array

Space complexity: O(min(M, N))

"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans=[]
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        set_num1 = set(nums1)
        for num in nums2:
            if num in set_num1:
                ans.append(num)
                set_num1.remove(num)
        return ans
                
