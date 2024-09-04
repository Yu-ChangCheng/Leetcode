class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # with 2D DP array O(m * n)
        dp = [[0] * (n + 1) for r in range(m+1)] 
        dp[m-1][n] = 1
        
        for r in range(m-1, -1 , -1):
            for c in range(n-1, -1, -1):
                dp[r][c] = dp[r+1][c] + dp[r][c+1]
        return dp[0][0]


        
        # with 1D DP array only O(n)
        rows = [1] * n

        for i in range(m-1):
            new_rows = [1] * n
            for j in range(n-2, -1, -1):   
                new_rows[j] = new_rows[j + 1] + rows[j] # add right and below
            rows = new_rows
        return rows[0]