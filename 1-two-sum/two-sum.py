class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_complement = defaultdict(int)

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in dict_complement:
                dict_complement[nums[i]] = i
            else:
                return [dict_complement[complement],i]
                
