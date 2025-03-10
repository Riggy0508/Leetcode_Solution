// https://leetcode.com/problems/01-matrix

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row,col=len(mat),len(mat[0])
        
        q=collections.deque()
        
        for x in range(row):
            for y in range(col):
                if mat[x][y]==0:
                    q.append((x,y,1))
                    
                    
        return self.bfs(row,col,q,mat)
    
    
    
    def bfs(self,row,col,q,mat):
        visited=set()
        
        while q:
            x,y,dist=q.popleft()
            
            for nx,ny in [[x+1,y], [x-1,y], [x,y+1], [x,y-1]]:
                if 0<=nx<row and 0<=ny<col and (nx,ny) not in visited:
                    if mat[nx][ny]==1:
                        visited.add((nx,ny))
                        mat[nx][ny]=dist
                        q.append((nx,ny,dist+1))
                        
        return mat
        