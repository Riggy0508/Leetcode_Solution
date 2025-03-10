// https://leetcode.com/problems/merge-strings-alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        n=max(len(word1),len(word2))
        result=[]

        for i in range(n):
            if i<len(word1):
                result.append(word1[i])
            if i<len(word2):
                result.append(word2[i])

        return "".join(result)