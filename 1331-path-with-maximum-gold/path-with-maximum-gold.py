class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])

        def dfs(i, j, visited):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0 or visited[i][j] == True:
                return 0
            
            visited[i][j] = True

            max_gold = 0
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0,-1)]:
                max_gold = max(max_gold, dfs(i+dx, j+dy, visited))

            visited[i][j] = False

            return grid[i][j] + max_gold

        max_gold = 0
        visited = [[False for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    max_gold = max(max_gold, dfs(i, j, visited))
        return max_gold

