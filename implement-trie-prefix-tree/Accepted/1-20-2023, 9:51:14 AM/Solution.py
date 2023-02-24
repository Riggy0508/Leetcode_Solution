// https://leetcode.com/problems/implement-trie-prefix-tree

class TrieNode:
    def __init__(self):
        self.endOfWord=False
        self.children={}

class Trie:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        cur=self.root
        for w in word:
            if not w in cur.children:
                cur.children[w]=TrieNode()
            cur=cur.children[w]
        cur.endOfWord=True

    def search(self, word: str) -> bool:
        cur=self.root
        for w in word:
            if not w in cur.children:
                return False
            cur=cur.children[w]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur=self.root

        for p in prefix:
            if p not in cur.children:
                return False
            cur=cur.children[p]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)