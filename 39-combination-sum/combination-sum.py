class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        curr = []

        def backtracking(i, curr, currSum):
            if i == len(candidates) or currSum > target:
                return
            if currSum == target:
                self.res.append(curr[:])
                return
            curr.append(candidates[i])
            backtracking(i, curr, currSum + candidates[i])
            curr.pop()
            backtracking(i+1, curr, currSum)
        
        backtracking(0, curr, 0)
        return self.res
        