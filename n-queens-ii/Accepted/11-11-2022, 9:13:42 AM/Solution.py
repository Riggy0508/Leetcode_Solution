// https://leetcode.com/problems/n-queens-ii

class Solution:
    def totalNQueens(self, n: int) -> int:
        cols=set()
        pos_diag=set()
        neg_diag=set()
        
        def backtrack(row,cols,pos_diag,neg_diag):
            if row==n:
                return 1
            
            total=0
            
            for col in range(n):
                # cur_pos_diag=(row+col)
                # cur_neg_diag=(row-col)
                
                if col in cols or (row+col) in pos_diag or (row-col) in neg_diag:
                    continue
                
                cols.add(col)
                pos_diag.add(row+col)
                neg_diag.add(row-col)
                
                total+=backtrack(row+1,cols,pos_diag,neg_diag)
                
                cols.remove(col)
                pos_diag.remove(row+col)
                neg_diag.remove(row-col)
                
            return total
                
        
        
        
        
        
        
        return backtrack(0,cols,pos_diag,neg_diag)
        
        