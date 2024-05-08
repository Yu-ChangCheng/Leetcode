class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.res = []
        curr =[]

        def backtracking(i, curr):
            if i == len(nums):
                self.res.append(curr[:])
                return
            
            curr.append(nums[i])
            backtracking(i+1, curr)
            curr.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtracking(i+1, curr)

        backtracking(0,curr)
        return self.res