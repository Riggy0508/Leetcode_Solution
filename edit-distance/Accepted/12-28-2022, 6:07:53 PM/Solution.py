// https://leetcode.com/problems/edit-distance

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        #We need to create our dp array which is gonna be 2d

        dp=[[float("inf")]*(len(word2)+1) for i in range(len(word1)+1)]

        for i in range(len(word1)+1):
            dp[i][len(word2)]=len(word1)-i
        for j in range(len(word2)+1):
            dp[len(word1)][j]=len(word2)-j
 
        #Now that we have filled our dp array. We are gonna use the bottom up approach in order to solve this question. For that we need to traverse backwards.

        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i]==word2[j]:
                    dp[i][j]=dp[i+1][j+1]
                else:
                    #The three operations that we can do right now is insert,update,delete
                    #insert#Replace#Delete
                    dp[i][j]=1+min(dp[i+1][j],dp[i+1][j+1],dp[i][j+1])
        return dp[0][0]

        return 1