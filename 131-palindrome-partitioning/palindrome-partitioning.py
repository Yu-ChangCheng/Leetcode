class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        part = []

        def isPali(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        def backtracking(i):
            if i == len(s):
                res.append(part[:])
                return
            
            for j in range(i, len(s)):
                if isPali(s, i, j):
                    part.append(s[i:j+1])
                    backtracking(j+1)
                    part.pop()
        backtracking(0)
        return res
