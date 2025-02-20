// https://leetcode.com/problems/goat-latin

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        def proc(idx,word):
            if word[0] not in "aeiouAEIOU":
                word=word[1:]+word[0]
            return word+"ma"+('a'*idx)
            
        return " ".join([proc(i,w) for i,w in enumerate(sentence.split(),1)])