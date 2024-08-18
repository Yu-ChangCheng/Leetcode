class TrieNode:
    def __init__(self):
        self.children = {}
        self.EndofWord = False

    def addWord(self,word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.EndofWord = True
class Solution(object):
    
    def findWords(self, board, words):
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        ROWS, COLS = len(board), len(board[0])
        res = set()

        def dfs(r,c,node,word):
            if ( r < 0 or c < 0 or  r == ROWS or c == COLS or board[r][c] not in node.children):
                return
        
            tempChar = board[r][c]
            board[r][c] = "#"
            node = node.children[tempChar]
            word+= tempChar
            if node.EndofWord:
                res.add(word)
                # node.EndofWord = False

            dfs(r-1,c,node,word)
            dfs(r+1,c,node,word)
            dfs(r,c-1,node,word)
            dfs(r,c+1,node,word)
            board[r][c] = tempChar
            
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")
        return list(res) 
