class Solution(object):
    def largestNumber(self, nums):
        nums = list(map(str, nums))

        def compare(N1, N2):
            if N1 + N2 >= N2 + N1:
                return -1
            else:
                return 1
        
        nums = sorted(nums, key = cmp_to_key(compare))
        if nums[0] == "0": return '0'
        return "".join(nums)