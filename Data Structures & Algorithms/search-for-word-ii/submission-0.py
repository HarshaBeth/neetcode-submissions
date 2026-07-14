# First, we need a trie structure to keep track of the words we are looking for
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        # Add the words to the Trie structure
        for w in words:
            root.addWord(w)
        
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        # Do backtracking if the word exists to begin with
        def dfs(r, c, word, node):
            if (r < 0 or c < 0 or 
            r >= ROWS or c >= COLS or 
            (r,c) in visit or 
            board[r][c] not in node.children):
                return

            visit.add((r,c))

            # Bookkeeping stuff
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)

            # Now go all 4 directions
            dfs(r-1, c, word, node)
            dfs(r+1, c, word, node)
            dfs(r, c-1, word, node)
            dfs(r, c+1, word, node)

            visit.remove((r,c))
        
        # Now run through the board
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, "", root)

        return list(res)











