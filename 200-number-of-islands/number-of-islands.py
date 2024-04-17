class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if r in range(rows) and c in range(cols):
                if grid[r][c] == "1":
                    grid[r][c] = "#"
                elif grid[r][c] != "1":
                    return
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
            return


        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r,c)
        return count
