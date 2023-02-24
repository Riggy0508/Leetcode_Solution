// https://leetcode.com/problems/n-queens

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        pos_diag=set()
        neg_diag=set()
        
        output=[]
        board=[["."]*n for i in range(n)]
        
        def backtrack(r):
            if r==n:
                curr=["".join(row) for row in board]
                output.append(curr.copy())
                return output
            
            for c in range(n):
                if c in col or (r+c) in pos_diag or (r-c) in neg_diag:
                    continue
                    
                col.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)
                board[r][c]="Q"
                
                backtrack(r+1)
                
                col.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)
                board[r][c]="."
                

        backtrack(0)
        return output
        