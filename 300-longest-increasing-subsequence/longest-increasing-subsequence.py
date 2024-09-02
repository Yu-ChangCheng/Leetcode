class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [0,1,2,3,4]
        # LIS[4] = 1
        # LIS[3] = max(1, 1 + LIS[4]) = 2
        # LIS[2] = max(1, 1 + LIS[3], 1 + LIS[4]) if LIS[2] < LIS[3] and LIS[2] < LIS[4]
        LIS = [1] * len(nums)
        res = 1
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1+LIS[j])
                    res = max(res, LIS[i])
        return res

        # O(N^2)
        # O(N)
















        if not nums:
            return 0
        
        # Initialize an array to store the smallest tail value
        # for increasing subsequences of various lengths.
        tails = []

        def binary_search(tails, target):
            left, right = 0, len(tails) - 1
            while left <= right:
                mid = (left + right) // 2
                if tails[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        for num in nums:
            # Find the insertion point using the custom binary search function
            idx = binary_search(tails, num)
            
            # If num is larger than all elements in tails,
            # append it to the end.
            if idx == len(tails):
                tails.append(num)
            else:
                # Otherwise, replace the element at the insertion point.
                tails[idx] = num
        
        # The length of the tails array will be the length of the
        # longest increasing subsequence.
        return len(tails)

        # Time Complexity: O(N log N)
        # Space Complexity: O(N)