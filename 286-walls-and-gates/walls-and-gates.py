class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        ROWS = len(rooms)
        COLS = len(rooms[0])
        q = deque()
        empty = 0
        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == 0:
                    q.append((i,j))
        
        direction = [(1,0), (0,1), (-1,0), (0,-1)]
        step = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direction:
                    nr, nc = r + dr, c + dc    
                    if nr < 0 or nr > ROWS - 1 or nc < 0 or nc > COLS - 1 or rooms[nr][nc] != 2147483647:
                        continue
                    elif rooms[nr][nc] == 2147483647:
                        rooms[nr][nc] = step
                        q.append((nr,nc))
            step += 1
            
        return rooms