class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        path = ""
        res = []

        def dfs(openN, closeN, path):
            if openN == closeN == n:
                res.append(path)
                return
            
            if openN < n:
                dfs(openN+1, closeN, path + "(")

            if closeN < openN:
                dfs(openN, closeN+1, path + ")")

        dfs(0,0,path)
        return res
