class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # matrix.reverse()

        # for i in range(len(matrix)):
        #     for j in range(i):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        l = 0
        r = len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                
                # store top left
                temp = matrix[top][l + i]

                # shift bottom left to top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # shift bottom right to bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # shift top right to bottom left
                matrix[bottom][r - i] = matrix[top + i][r]

                # shift top left (temp) to top right
                matrix[top + i][r] = temp
            l += 1
            r -= 1


