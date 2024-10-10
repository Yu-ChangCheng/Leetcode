class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):
            if 0 <= r < rows and 0 <= c < cols:
                if grid[r][c] == "1":
                    grid[r][c] = "#"
                else:
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

                
        count = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols:
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

        
        
        def bfs(r, c):
            # Initialize the queue with the starting cell and mark it as visited
            q = deque([(r, c)])
            grid[r][c] = "#"
            while q:
                r, c = q.popleft()
                # Check all four possible directions
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    # Make sure the new cell is within bounds
                    if 0 <= nr < rows and 0 <= nc < cols:
                        # Check if the cell is part of an island and not visited
                        if grid[nr][nc] == "1":
                            # Mark the cell as visited and enqueue it
                            grid[nr][nc] = "#"
                            q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    bfs(r, c)
        return count
        

        def dfs(r, c):
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '1':
                    grid[r][c] = "#"  # Mark the cell as visited
                    # Push all adjacent cells to the stack
                    stack.append((r + 1, c))
                    stack.append((r - 1, c))
                    stack.append((r, c + 1))
                    stack.append((r, c - 1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        return count
           













