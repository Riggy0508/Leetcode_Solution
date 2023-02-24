// https://leetcode.com/problems/n-queens

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #In order to check track of the queens, and take care that no two queens are placed in same row or same col or positive-diagonal or negative-diagonal
        #Before solving this question one should also know that the fact that, every positive diagon have the same property as (r+c) and negative_diag as (r-c)
        
        cols=set()
        pos_diag=set()
        neg_diag=set()
        
        res=[] # this is gonna be our output list which we are gonna return
        #first we are gonna start with making the board 
        board=[["."]*n for i in range(n)]
        
        
        #in our backtrack we are gonna use r as the row that we wanna work on
        def backtrack(r):
            if r==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return
            
            #Because we know that we our column size if also gonna be equal to n
            for c in range(n):
                
                #we are checking if the queen is already presend in the pos_dia or neg_dia or in the same column if so we are gonna skip it and move to the next one
                if c in cols or (r+c) in pos_diag or (r-c) in neg_diag:
                    continue
                
                cols.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)
                board[r][c]="Q"
                
                backtrack(r+1)
                
                cols.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)
                board[r][c]="."
                
        backtrack(0)
        return res
        