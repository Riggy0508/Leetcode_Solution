// https://leetcode.com/problems/maximum-score-after-splitting-a-string

class Solution:
    def maxScore(self, s: str) -> int:
        maxS=0

        for i in range(1,len(s)):
            left=s[:i]
            right=s[i:]
            maxS=max(maxS,left.count("0")+right.count("1"))
        

        return maxS