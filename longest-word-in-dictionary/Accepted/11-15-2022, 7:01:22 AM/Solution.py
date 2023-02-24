// https://leetcode.com/problems/longest-word-in-dictionary

class TrieNode:
    def __init__(self):
        self.endOfWord=False
        self.children={}
        
class Trie:
    def __init__(self):
        self.root=TrieNode()
        
    def insert(self,word):
        cur=self.root
        
        for w in word:
            if not w in cur.children:
                cur.children[w]=TrieNode()
            cur=cur.children[w]
        cur.endOfWord=True
        
    def search(self,word):
        cur=self.root
        
        for w in word:
            if not w in cur.children:
                return False
            cur=cur.children[w]
            if not cur.endOfWord:
                return False
        return cur.endOfWord

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie=Trie()
        longest_word=""
        
        for w in words:
            trie.insert(w)
            
        for w in words:
            if trie.search(w):
                if len(w) > len(longest_word):
                    longest_word=w
                elif len(w)==len(longest_word):
                    longest_word=w if w<longest_word else longest_word
        return longest_word
            