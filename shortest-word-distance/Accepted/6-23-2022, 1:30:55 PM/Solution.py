// https://leetcode.com/problems/shortest-word-distance

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        one,two=-1,-1
        minDist=len(wordsDict)
        
        for i in range(len(wordsDict)):
            if wordsDict[i]==word1:
                one=i
            elif wordsDict[i]==word2:
                two=i
                
            if one!=-1 and two!=-1:
                minDist=min(minDist,abs(one-two))
        return minDist