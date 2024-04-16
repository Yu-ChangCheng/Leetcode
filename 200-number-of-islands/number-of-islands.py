class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        if not grid: return 0

        def dfs(i, j):
            if i in range(len(grid)) and j in range(len(grid[0])):
                if grid[i][j]!= "1":
                    return
                if grid[i][j] == "1":
                    grid[i][j] = "#"

                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)
            return

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        return count
             
        
    
