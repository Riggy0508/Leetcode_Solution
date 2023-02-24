// https://leetcode.com/problems/break-a-palindrome

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        li=list(palindrome)
        n=len(li)
        if n==1:
            return ""

        for i in range(n):
            if li[i]!='a':
                li[i]='a'
                break
        
        return "".join(li)
