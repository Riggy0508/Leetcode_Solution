// https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited=set()
        rows,cols=len(grid),len(grid[0])
        
        
        
        
        def bfs(r,c):
            directions=[(0,1),(1,0),(-1,0),(0,-1)]
            q=collections.deque()
            q.append((r,c))
            
            
            while q:
                row,col=q.popleft()
                
                for dr,dc in directions:
                        r,c=dr+row,dc+col
                        
                        if r in range(rows) and c in range(cols) and grid[r][c]=="1" and (r,c) not in visited:
                            q.append((r,c))
                            visited.add((r,c))
        
        
        
        islands=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    islands+=1
                    bfs(r,c)
        
        return islands
                    
        