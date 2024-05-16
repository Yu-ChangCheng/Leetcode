class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1
        val = 1
        matrix = [[0] * n for _ in range(n)]

        while left <= right and top <= bottom:
            # left to right
            for c in range(left, right + 1):
                matrix[top][c] = val
                val += 1
            top += 1

            # top to bottom
            for r in range(top, bottom + 1):
                matrix[r][right] = val
                val += 1
            right -= 1

            # right to left
            for c in range(right, left - 1, -1):
                matrix[bottom][c] = val
                val += 1
            bottom -= 1

            # bottom to top
            for r in range(bottom, top - 1, -1):
                matrix[r][left] = val
                val += 1
            left += 1

        return matrix
