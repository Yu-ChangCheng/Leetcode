class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr[:])                
                return 
            if total > target or i >= len(candidates):
                return
            
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            curr.pop()
            dfs(i+1, curr, total)

        dfs(0, [], 0)
        return res