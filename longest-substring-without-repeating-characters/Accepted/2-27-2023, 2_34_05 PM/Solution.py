// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset=set()

        l=0
        maxL=0

        for r in  range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            
            charset.add(s[r])
            maxL=max(maxL,r-l+1)
        return maxL
