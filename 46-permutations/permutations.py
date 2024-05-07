class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res =[]
        curr = []
        def backtracking(curr):
            if len(curr) == len(nums):
                self.res.append(curr[:])
                return
            
            for n in nums:
                if n not in curr:
                    curr.append(n)
                    backtracking(curr)
                    curr.pop()
        backtracking(curr)
        return self.res