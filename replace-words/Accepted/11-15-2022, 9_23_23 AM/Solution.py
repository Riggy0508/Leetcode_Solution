// https://leetcode.com/problems/replace-words

class TrieNode(object):
        def __init__(self):
            self.children = {}
            self.isWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isWord = True
        
    def transfer(self,word):
        cur=self.root
        string=""
        for char in word:
            if cur.isWord:
                return string
            if char not in cur.children:
                return word
            string+=char
            cur=cur.children[char]
        return word
            

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        output=[]
        words=sentence.split(" ")
        trie=Trie()
        
        for word in dictionary:
            trie.insert(word)
            
        for word in words:
            output.append(trie.transfer(word))
        return " ".join(output)