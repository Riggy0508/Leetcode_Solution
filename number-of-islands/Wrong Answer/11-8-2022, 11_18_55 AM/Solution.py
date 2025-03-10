// https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])
        
        islands=0
        
        visited=set()
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        
        #One should notice that as we are using bfs we have to make use of queue
        
        
        def bfs(r,c):
            q=collections.deque()
            visited.add((r,c))
            q.append((r,c))
            
            #check if the neighbouring [r][c] is not in visited set and if not increase the island counter 
            
            while q:
                row,col=q.popleft()
                for dr,dc in directions:
                    r=row+dr
                    c=col+dc
                    
                    if r in range(rows) and c in range(cols) and (r,c) not in visited:
                        q.append((r,c))
                        visited.add((r,c))
                    
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    islands+=1
                    bfs(r,c)
        return islands