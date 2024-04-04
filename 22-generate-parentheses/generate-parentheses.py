class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        path = ""
        openN = 0
        closeN = 0 
        res = []

        def DFS(openN, closeN, path):
            if n == openN == closeN:
                res.append(path)
                return
            if n >= openN and openN >= closeN:
                DFS(openN+1, closeN, path + "(")

            if n >= closeN and closeN <= openN:
                DFS(openN, closeN+1, path + ")")
        
        DFS(0,0,path)
        return res