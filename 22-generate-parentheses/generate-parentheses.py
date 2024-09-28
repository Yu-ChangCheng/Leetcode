class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        path = ""
        res = []

        def DFS(openN, closeN, path):
            if n == openN == closeN:
                res.append(path)
                return
            if n > openN and openN >= closeN:
                DFS(openN + 1, closeN, path + "(")
            if n > closeN and openN >= closeN:
                DFS(openN, closeN + 1, path + ")")
        DFS(0,0,path)
        return res


        # path = ""
        # res = []

        # def DFS(openN, closeN, path):
        #     if n == openN == closeN:
        #         res.append(path)
        #         return

        #     if n > openN and openN >= closeN:
        #         DFS(openN+1, closeN, path + "(")
        #     if n > closeN and openN >= closeN:
        #         DFS(openN, closeN+1, path + ")")
        # DFS(0,0,path)    
        # return res