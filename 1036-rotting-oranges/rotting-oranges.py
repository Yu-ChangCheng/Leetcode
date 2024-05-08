class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = deque()
        fresh = 0
        time = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] != 1:
                        continue
                    if grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            time += 1
        return time if not fresh else -1        



