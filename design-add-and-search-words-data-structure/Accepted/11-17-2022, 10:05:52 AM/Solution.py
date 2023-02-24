// https://leetcode.com/problems/design-add-and-search-words-data-structure

class TrieNode:
    def __init__(self):
        self.children={}  #This is a trieNode
        self.endOfWord=False    

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        self.max_len=0

    def addWord(self, word: str) -> None:
        cur=self.root
        for w in word:
            if w not in cur.children:
                cur.children[w]=TrieNode()
            cur=cur.children[w]
        cur.endOfWord=True
        self.max_len=max(self.max_len,len(word))

    def search(self, word: str) -> bool:
        if len(word)>self.max_len:
            return False
        def dfs(j,root):
            cur=root
            for i in range(j,len(word)):
                w=word[i]
                if w ==".":
                    for child in cur.children.values():
                        #print(child.children)
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if w not in cur.children:
                        return False
                    cur=cur.children[w]
            return cur.endOfWord
        return dfs(0,self.root)
    
    
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)