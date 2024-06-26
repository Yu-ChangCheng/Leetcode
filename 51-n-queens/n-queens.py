class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        col_set = set()
        pos_diag_set = set() # (r-c) as r - c will be the key for the diag -3, -2, -1,  0,  1,  2,  3
        neg_diag_set = set() # (r+c) as r + c will be the key for the diag  0,  1,  2,  3,  4,  5,  6
        res = []
        board = [["."] * n for r in range(n)] # 

        def backtracking(r):
            # base case
            if r == n:
                temp = []
                for r in range(n):
                    row_string = "".join(board[r])
                    temp.append(row_string)
                res.append(temp)

            # iterate column for rows 
            for c in range(n):
                if c in col_set or (r-c) in pos_diag_set or (r+c) in neg_diag_set:
                    continue

                # add to the set for the current row
                col_set.add(c)
                pos_diag_set.add(r-c)
                neg_diag_set.add(r+c)
                board[r][c] = "Q"
                
                # iterate thorugh every row
                backtracking(r+1)

                # remove r, and c from the board
                col_set.remove(c)
                pos_diag_set.remove(r-c)
                neg_diag_set.remove(r+c)
                board[r][c] = "."
        
        backtracking(0)
        return res