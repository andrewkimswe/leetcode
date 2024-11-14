class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        return self._search_in_node(word, 0, self.root)
    
    def _search_in_node(self, word: str, index: int, node: TrieNode) -> bool:
        if index == len(word):
            return node.isEndOfWord
        
        char = word[index]
        
        if char == '.':
            for child in node.children.values():
                if self._search_in_node(word, index + 1, child):
                    return True
            return False
        else:
            if char not in node.children:
                return False
            return self._search_in_node(word, index + 1, node.children[char])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)