class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(heights)
        cols = len(heights[0])
        pac_set = set()
        alt_set = set()

        def dfs(r, c, visited_set, prev_val):
            if ((r,c) in visited_set or r < 0 or c < 0 or r == rows  or c == cols or heights[r][c] < prev_val):
                return  
            visited_set.add((r,c))
            dfs(r+1, c, visited_set, heights[r][c])
            dfs(r-1, c, visited_set, heights[r][c])
            dfs(r, c+1, visited_set, heights[r][c])
            dfs(r, c-1, visited_set, heights[r][c])

        for c in range(cols):
            dfs(0, c, pac_set, heights[0][c])
            dfs(rows-1, c, alt_set, heights[rows-1][c])
        
        for r in range(rows):
            dfs(r, 0 , pac_set,heights[r][0])
            dfs(r, cols-1, alt_set, heights[r][cols-1])

        res = []
        for (pac_x, pac_y) in pac_set:
            if (pac_x, pac_y) in alt_set:
                res.append([pac_x, pac_y])

        return res