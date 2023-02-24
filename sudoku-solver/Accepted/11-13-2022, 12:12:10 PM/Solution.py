// https://leetcode.com/problems/sudoku-solver

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def backtrack(r,c):
            if c==9:
                r=r+1
                c=0
            if r==9:
                return True
            
            if board[r][c]!=".":
                return backtrack(r,c+1)
            
            for val in range(1,10):
                if not (val in rows[r] or val in cols[c] or val in square[(r//3,c//3)]):
                    rows[r].add(val)
                    cols[c].add(val)
                    square[(r//3,c//3)].add(val)
                        
                    board[r][c]=str(val)
                        
                    if backtrack(r,c+1): 
                        return 1
                        
                    rows[r].remove(val)
                    cols[c].remove(val)
                    square[(r//3,c//3)].remove(val)
                        
                    board[r][c]="."
            return 0
                        

        rows=defaultdict(set)
        cols=defaultdict(set)
        square=defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if (board[r][c]!="."):
                    rows[r].add(int(board[r][c]))
                    cols[c].add(int(board[r][c]))
                    square[(r//3,c//3)].add(int(board[r][c]))
                else:
                    continue
        backtrack(0,0)
        