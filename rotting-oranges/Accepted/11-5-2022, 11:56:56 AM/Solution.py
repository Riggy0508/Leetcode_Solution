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
                                               
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        queue=deque()
        
        fresh_oranges=0
        
        ROWS,COLS=len(grid),len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    queue.append((r,c))
                elif grid[r][c]==1:
                    fresh_oranges+=1
        
        queue.append((-1,-1))
        
        ##Starting the rooting process via BFS
        minutes_passed=-1
        
        directions=[(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            row,col=queue.popleft()
            if row==-1:
                minutes_passed+=1
                if queue:
                    queue.append((-1,-1))
                    
            else:
                #We now come to a place where this is a rotten orange
                #which will eventually rot the neighbouring oranges
                for d in directions:
                    neighbor_row,neighbor_col=row+d[0],col+d[1]
                    if ROWS>neighbor_row>=0 and COLS>neighbor_col>=0:
                        if grid[neighbor_row][neighbor_col]==1:
                            grid[neighbor_row][neighbor_col]=2
                            fresh_oranges-=1
                            
                            queue.append((neighbor_row,neighbor_col))
                            
        return minutes_passed if fresh_oranges==0 else -1
                            