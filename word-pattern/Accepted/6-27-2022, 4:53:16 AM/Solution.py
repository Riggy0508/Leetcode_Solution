// https://leetcode.com/problems/word-pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split(" ")
        if len(pattern)!=len(words):
            return False
        
        charToWord,wordToChar={},{}
        
        for i in range(len(pattern)):
            c1,c2=pattern[i],words[i]
            
            if (c1 in charToWord and charToWord[c1]!=c2):
                return False
            elif(c2 in wordToChar and wordToChar[c2]!=c1):
                return False
            charToWord[c1]=c2
            wordToChar[c2]=c1
        return True
        