// https://leetcode.com/problems/reverse-words-in-a-string-iii

class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        d=[]
        
        for words in s:
            d.append(words[::-1])
        return " ".join(d)