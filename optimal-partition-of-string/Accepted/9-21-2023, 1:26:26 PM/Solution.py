// https://leetcode.com/problems/optimal-partition-of-string

class Solution:
    def partitionString(self, s: str) -> int:
        
        curSet=set()
        res=1

        for char in s:
            if char in curSet:
                res+=1
                curSet=set()
            curSet.add(char)
        return res