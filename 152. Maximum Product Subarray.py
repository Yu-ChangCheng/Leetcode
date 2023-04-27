class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)
        cur_max = 1
        cur_min = 1

        for n in nums:
            if n == 0:
                cur_max = 1
                cur_min = 1

            cur_max, cur_min = max(cur_max*n, cur_min*n, n), min(cur_max*n, cur_min*n, n)
            res = max(cur_max, res)

        return res
