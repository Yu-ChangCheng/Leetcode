class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row, col = len(board), len(board[0])
        R, C, seen = range(row), range(col), set()

        def dfs(coord, i=0):
            
            if len(word) == i: return True
            
            r,c = coord

            if (r not in R or c not in C or 
                coord in seen            or 
                board[r][c] != word[i]): return False
            
            seen.add(coord)

            res = (dfs((r+1,c), i+1) or dfs((r,c+1), i+1) or
                   dfs((r-1,c), i+1) or dfs((r,c-1), i+1))
            
            seen.remove(coord)

            return res

        boardCt, wrdCt = Counter(chain(*board)), Counter(word)
        if any (boardCt[ch] < wrdCt[ch] for ch in wrdCt): return False

        if boardCt[word[0]] > boardCt[word[-1]]: word = word[::-1]
        
        return any(dfs((r, c))  for c in C for r in R)