class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def backtracking(i, curr, curr_sum):
            if i >= len(candidates) or curr_sum > target:
                return 
            if curr_sum == target:
                res.append(curr[:])
                return
    
            curr.append(candidates[i])
            backtracking(i, curr, curr_sum + candidates[i])
            curr.pop()
            backtracking(i+1, curr, curr_sum)

        backtracking(0, [], 0)
        return res