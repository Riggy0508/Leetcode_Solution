// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        hash1={}
        maxL=0


        for r in range(len(s)):
            while s[r] in hash1:
                del hash1[s[l]]
                l+=1
            hash1[s[r]]=1
            maxL=max(maxL,r-l+1)

        return maxL