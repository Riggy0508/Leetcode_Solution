// https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        
        islands=0
        
        grid.append(['0']*(cols+1))
        for i in range(rows):
            grid[i].append('0')
            
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    self.mark_neighbour(grid,i,j)
                    islands+=1
                    
        return islands
    
    
    
    
    def mark_neighbour(self,grid,i,j):
        q=collections.deque()
        grid[i][j]=="2"
        q.append((i,j))
        
        while q:
            (i,j)=q.popleft()
            if grid[i-1][j]=="1":
                grid[i-1][j]="2"
                q.append((i-1,j))
            if grid[i+1][j]=="1":
                grid[i+1][j]="2"
                q.append((i+1,j))
            if grid[i][j-1]=="1":
                grid[i][j-1]="2"
                q.append((i,j-1))
            if grid[i][j+1]=="1":
                grid[i][j+1]="2"
                q.append((i,j+1))
            
            