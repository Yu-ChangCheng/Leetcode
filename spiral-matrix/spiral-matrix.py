class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        x, y, dx, dy = 0, 0, 1, 0
        m = len(matrix)
        n = len(matrix[0])
        res = []
        for _ in range(m*n):

            if not 0 <= x+dx < n or not 0 <= y+dy < m or matrix[y+dy][x+dx] == "*":
                dx, dy = -dy, dx

            res.append(matrix[y][x])
            matrix[y][x] = "*"
            x, y = x+dx, y+dy
            
        return res