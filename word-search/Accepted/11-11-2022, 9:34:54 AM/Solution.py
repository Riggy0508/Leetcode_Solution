// https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        
        path=set()
        
        def backtrack(row,col,i):
            if i==len(word):
                return True
            
            if row<0 or row>=rows or col<0 or col>=cols or board[row][col]!=word[i] or (row,col) in path:
                return False
            
            path.add((row,col)) 
            
            res=(backtrack(row-1,col,i+1) or
                          backtrack(row+1,col,i+1) or
                                   backtrack(row,col-1,i+1) or
                                            backtrack(row,col+1,i+1))
                                             
            path.remove((row,col))
            return res
        
        
        
        for row in range(rows):
            for col in range(cols):
                if backtrack(row,col,0):
                    return True
                
        return False
                