class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r,c,i):
            if i == len(word):    # base case if matched the len, meaning we found the word
                return True
            # if out of bound or not matched return False
            if r < 0 or r > ROWS - 1 or c < 0 or c > COLS - 1 or board[r][c] != word[i]:
                return False
            temp = board[r][c]      # store a temp char before backtracking
            board[r][c] = "#"       # mark current node as visited
            result = (              # DFS visit the neighbors
                dfs(r+1, c, i+1) or 
                dfs(r-1, c, i+1) or
                dfs(r, c+1, i+1) or
                dfs(r, c-1, i+1)
            )
            board[r][c] = temp      # restore the temp char after backtracking 
            return result

        result = False
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    result = dfs(r, c, 0)
                if result:
                    return True
        return False
        # TC: O(m * n * 4^len(word)) for each cell in the board, where DFS can have a depth of up to len(word) in four directions
        # SC: O(len(word)) for the DFS call stack  

