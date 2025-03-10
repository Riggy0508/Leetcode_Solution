// https://leetcode.com/problems/reverse-words-in-a-string-iii

class Solution:
    def reverseWords(self, s: str) -> str:
        res=[]
        l=0
        r=0

        while r<len(s):
            if s[r]==" ":
                cur_word=s[l:r]
                res.append(cur_word[::-1])
                l=r+1
            r+=1

        res.append(s[l:r][::-1])
        return " ".join(res)