class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        res = 0

        for n in num_set:
            if n - 1 not in num_set:
                sequence_length = 1
                while n + 1 in num_set:
                    sequence_length += 1
                    n += 1
                res = max(res,sequence_length)
        return res

        num_set = set(nums)
        res = 0

        for n in num_set:
            # start a sequence
            if n - 1 not in num_set:
                sequence_length = 1 
                while n + 1 in num_set:
                    sequence_length += 1
                    n += 1
                res = max(res, sequence_length)
        return res
