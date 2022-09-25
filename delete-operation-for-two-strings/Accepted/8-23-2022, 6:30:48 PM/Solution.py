// https://leetcode.com/problems/delete-operation-for-two-strings

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        a=[]
        
        a=[[0]*(n+1) for i in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                if word1[i]==word2[j]:
                    a[i+1][j+1]=1+a[i][j]
                else:
                    a[i+1][j+1]=max(a[i][j+1],a[i+1][j])
        
        return m+n-(2*a[-1][-1])