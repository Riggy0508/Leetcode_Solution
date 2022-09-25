// https://leetcode.com/problems/count-binary-substrings

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n=len(s)
        prev,cur=0,1
        output=0
        for i in range(1,n):
            if s[i]!=s[i-1]:
                output+=min(cur,prev)
                prev=cur
                cur=1
            else:
                cur+=1
        return output+min(prev,cur)