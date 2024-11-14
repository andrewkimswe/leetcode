class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None 

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        result = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self._dfs(board, i, j, trie.root, result)
        return result

    def _dfs(self, board, i, j, node, result):
        if node.word:
            result.append(node.word)
            node.word = None
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] not in node.children:
            return

        char = board[i][j]
        board[i][j] = "#"
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            self._dfs(board, ni, nj, node.children[char], result)
        
        board[i][j] = char

        if not node.children[char].children:
            del node.children[char]