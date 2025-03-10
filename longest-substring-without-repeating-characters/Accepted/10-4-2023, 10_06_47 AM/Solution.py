// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet=set()
        l=0
        maxL=0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            maxL=max(maxL,r-l+1)
        return maxL