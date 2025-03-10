// https://leetcode.com/problems/rotting-oranges

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        #Count the number of fresh oranges and rotten oranges
        q=collections.deque()
        
        fresh=0
        ROWS,COLS=len(grid),len(grid[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    q.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1
                    
        
        #Checking if any oranges are rotten and if they are, make the neig one rotten too. 
        time_lapsed=-1
        
        #Defining the directions which we can go into
        
        direction=[(-1,0),(1,0),(0,-1),(0,1)] 
        
        #Creating boundary/level so that we can increase the time_lapse each time we go onto the next level.
        q.append((-1,-1))
        while q:
            row,col=q.popleft()
            
            #Checking if we have gone to the next level because we need to maintain the timestamp
            if row==-1:
                time_lapsed+=1
                #Creating another boundary
                if q:
                    q.append((-1,-1))
            else:
                
                # Procedure to check in other direction's 
                for d in direction:
                    neigh_row,neigh_col=d[0]+row, d[1]+col
                    if ROWS>neigh_row>=0 and COLS>neigh_col>=0:
                        
                        #checking if the neighhour's are present and if they are fresh, rotten tem
                        if grid[neigh_row][neigh_col]==1:
                            grid[neigh_row][neigh_col]=2
                            fresh-=1
                            
                            q.append((neigh_row,neigh_col))
                            
        return time_lapsed if fresh==0 else -1
                        
            
        
                    