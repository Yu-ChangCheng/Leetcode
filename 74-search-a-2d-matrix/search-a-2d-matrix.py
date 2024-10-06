class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        TOP = 0
        BOTTOM = ROWS - 1
        l = 0 
        r = COLS - 1

        while TOP <= BOTTOM:
            MID = (TOP + BOTTOM) // 2
            if matrix[MID][0] > target: # if the start of the array larger than target (go up)
                BOTTOM = MID - 1
            elif matrix[MID][-1] < target: # if the end of the array less than target (go down)
                TOP = MID + 1
            else:
                break
        
        if TOP > BOTTOM:
            return False
        
        while l <= r:
            m = (l+r) // 2 
            if matrix[MID][m] > target: 
                r = m - 1
            elif matrix[MID][m] < target: 
                l = m + 1
            else:
                return True

        return False
