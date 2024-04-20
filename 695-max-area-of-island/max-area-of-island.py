class Solution(object):
    def __init__(self):
        self.maxArea = 0

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])

        def dfs(r, c):
            if not (0 <= r < row and 0 <= c < col) :
                return 0
            if grid[r][c] != 1:
                return 0

            grid[r][c] = "#"
            area = 1  # Start area calculation for this piece
            
            # Recursively add the area from neighboring cells
            area += dfs(r+1, c)
            area += dfs(r-1, c)
            area += dfs(r, c+1)
            area += dfs(r, c-1)
            return area

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    currArea = dfs(r,c)
                    self.maxArea = max(self.maxArea, currArea)

        return self.maxArea