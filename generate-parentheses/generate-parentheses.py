class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        s = ""
        res = []

        def dfs(openN, closeN, s):
            if openN == closeN == n:
                res.append(s)
                return
            
            if openN < n:
                dfs(openN+1, closeN, s + "(")

            if closeN < openN:
                dfs(openN, closeN+1, s + ")")

        dfs(0,0,s)
        return res
