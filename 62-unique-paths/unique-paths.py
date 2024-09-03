class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for r in range(m+1)] 
        dp[m-1][n] = 1
        print(dp)

        for r in range(m-1, -1 , -1):
            for c in range(n-1, -1, -1):
                dp[r][c] = dp[r+1][c] + dp[r][c+1]
        return dp[0][0]