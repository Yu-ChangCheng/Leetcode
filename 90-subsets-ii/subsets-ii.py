class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = set()
        curr =[]

        def backtracking(i, curr):
            if i == len(nums):
                self.res.add(tuple(sorted(curr[:])))
                return
            
            curr.append(nums[i])
            backtracking(i+1, curr)
            curr.pop()
            backtracking(i+1, curr)
        backtracking(0,curr)
        return self.res