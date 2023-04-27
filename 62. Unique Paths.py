class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        rows = [1] * n

        for i in range(m-1):
            new_rows = [1] * n
            for j in range(n-2, -1, -1):
                new_rows[j] = new_rows[j + 1] + rows[j] # add right and below
            rows = new_rows
        return rows[0]
