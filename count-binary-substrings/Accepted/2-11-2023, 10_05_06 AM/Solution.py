// https://leetcode.com/problems/count-binary-substrings

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans=0
        prev=0
        cur=1

        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                ans+=min(prev,cur)
                prev=cur
                cur=1
            else:
                cur+=1
        return ans+min(prev,cur)