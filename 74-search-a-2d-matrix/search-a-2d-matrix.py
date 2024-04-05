class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        TOP = 0
        BOTTOM = ROWS - 1
        l = 0
        r = COLS - 1

        while TOP <= BOTTOM:
            MID = (TOP+BOTTOM) // 2
            if matrix[MID][0] > target:
                BOTTOM = MID - 1
            elif matrix[MID][-1] < target:
                TOP = MID + 1
            else:
                break
        
        if not (TOP <= BOTTOM):
            return False

        while l <= r:
            mid = (l + r) // 2
            if matrix[MID][mid] < target:
                l = mid + 1
            elif matrix[MID][mid] > target:
                r = mid - 1
            else:
                return True
        
        return False



