// https://leetcode.com/problems/n-queens-ii

class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row,diagonal,anti_diagonal,cols):
            if row==n:
                return 1
            
            solutions=0
            #checking if the queen is presetn in a given col. nxn matrix that's why we are checking in range(n)
            for col in range(n):
                cur_diagonal=row-col
                cur_anti_diagonal=row+col
                
                
                if col in cols or cur_diagonal in diagonal or cur_anti_diagonal in anti_diagonal:
                    continue
                    
                cols.add(col)
                diagonal.add(cur_diagonal)
                anti_diagonal.add(cur_anti_diagonal)
                
                solutions+=backtrack(row+1,diagonal,anti_diagonal,cols)
                
                cols.remove(col)
                diagonal.remove(cur_diagonal)
                anti_diagonal.remove(cur_anti_diagonal)
                
            return solutions
                
            
        return backtrack(0,set(),set(),set())