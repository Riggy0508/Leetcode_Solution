// https://leetcode.com/problems/maximum-number-of-fish-in-a-grid

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        res=0
        visit=set()


        def dfs(r,c):
            if r<0 or c<0 or r==ROWS or c==COLS or grid[r][c]==0 or (r,c) in visit:
                return 0

            visit.add((r,c))
            res=grid[r][c]
            neighbor=[[r+1,c],[r-1,c],[r,c-1],[r,c+1]]
            for nr,nc in neighbor:
                res+=dfs(nr,nc)
            
            return res

        for r in range(ROWS):
            for c in range(COLS):
                res=max(res,dfs(r,c))
        
        return res