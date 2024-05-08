class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        curr = []
        def backtracking(start, curr):
            if len(curr) == k:
                res.append(curr[:])
                return
            for i in range(start, n+1):
                curr.append(i)
                backtracking(i+1, curr)
                curr.pop()
        backtracking(1, curr)
        return res