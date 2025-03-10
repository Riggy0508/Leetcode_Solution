// https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*(len(s)+1)
        dp[len(s)]=True

        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if (i+len(w)<=len(s)) and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                if dp[i]:
                    break
        
        return dp[0]




#What we are essentially trying to do is we are checking the length of the word present into the dictionary and calculating it's length.
#Then we are trying to check if any word is present inside the string s for the same length. If it's present we are returning true. And we are doing so for each position of the string s. So ultimately at position 0 we will have our output. If you have any confusion please refer to the following video. It's pretty well explained. 
#https://www.youtube.com/watch?v=Sx9NNgInc3A