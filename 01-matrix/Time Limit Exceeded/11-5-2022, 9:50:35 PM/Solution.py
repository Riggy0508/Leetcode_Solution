// https://leetcode.com/problems/01-matrix

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows,cols=len(mat),len(mat[0])

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for row in range(rows):
            for col in range(cols):
                if mat[row][col]!=0:
                    q=collections.deque()
                    q.append((row,col,0))
                    
                    while q:
                        r,c,dist=q.popleft()
                        
                        if mat[r][c]==0:
                            break
                        if mat[r][c]!=0:
                            for d in directions:
                                nr=r+d[0]
                                nc=c+d[1]
                                
                                if nr<rows and nr>=0 and nc<cols and nc>=0:
                                    q.append((nr,nc,dist+1))
                            
                    mat[row][col]=dist
        return mat
                    
        