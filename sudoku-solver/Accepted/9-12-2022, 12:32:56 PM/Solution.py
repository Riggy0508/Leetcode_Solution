// https://leetcode.com/problems/sudoku-solver

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        choices=set({'1','2','3','4','5','6','7','8','9'})
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        sub_grid=[[set() for _ in range(3)] for _ in range(3)]
        
        
        jobs=[]
        
        for r, row in enumerate(board):
            sub_r=int(r/3)
            for c, cell in enumerate(row):
                sub_c=int(c/3)
                
                if cell!=".":
                    rows[r].add(cell)
                    cols[c].add(cell)
                    sub_grid[sub_r][sub_c].add(cell)
                
                else:
                    jobs.append((r,c))
                    
        self.solved=False
        
        def solve(job_num):
            r,c=jobs[job_num]
            sub_r=int(r/3)
            sub_c=int(c/3)
            
            options = choices ^ (rows[r] | cols[c] | sub_grid[sub_r][sub_c])
            
            for op in options:
                rows[r].add(op)
                cols[c].add(op)
                sub_grid[sub_r][sub_c].add(op)
                board[r][c]=op
                
                if job_num+1==len(jobs):
                    self.solved=True
                    
                else:
                    solve(job_num+1)
                    
                if self.solved:return
                
                
                rows[r].remove(op)
                cols[c].remove(op)
                sub_grid[sub_r][sub_c].remove(op)
                board[r][c]="."
                
        solve(0)