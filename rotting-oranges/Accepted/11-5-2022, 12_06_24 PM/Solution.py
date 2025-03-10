// https://leetcode.com/problems/rotting-oranges

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh=0
        
        q=collections.deque()
        ROWS,COLS=len(grid),len(grid[0])
        
        
        #Step 1: calculting the fresh oranges and the rotten oranges so that it can help us later on
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    q.append((r,c))
                if grid[r][c]==1:
                    fresh+=1
        
        
        q.append((-1,-1))
        
        #Because we have base 
        time_lapsed=-1
        directions=[(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        while q:
            row,col=q.popleft()
            if row==-1:
                time_lapsed+=1
                if q:
                    q.append((-1,-1))
            else:
                for d in directions:
                    neighbor_row,neighbor_col=d[0]+row,d[1]+col
                    if ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col]==1:
                            grid[neighbor_row][neighbor_col]=2
                            fresh-=1
                            
                            q.append((neighbor_row,neighbor_col))
                            
        return time_lapsed if fresh==0 else -1
                                               
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        