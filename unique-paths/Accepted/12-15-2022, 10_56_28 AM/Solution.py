// https://leetcode.com/problems/unique-paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*n for i in range(m)]


        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    dp[i][j]=1
                elif i>0 and j>0:
                    dp[i][j]+=(dp[i-1][j]+dp[i][j-1])

        return dp[m-1][n-1]



    #Reference: https://www.youtube.com/watch?v=IlEsdxuD4lY
    #Note: I am trying to do the opposite of what's shown in the video. 