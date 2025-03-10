// https://leetcode.com/problems/diagonal-traverse

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        

        if not mat:
            return 

        m,n=len(mat),len(mat[0])
        row,col,direction=0,0,1
        result=[]

        for _ in range(m*n):
            result.append(mat[row][col])
            if direction==1:
                if col==n-1:
                    row+=1
                    direction=-11
                elif row==0:
                    col+=1
                    direction=-1
                else:
                    row-=1
                    col+=1
                
            else:
                if row==m-1:
                    col+=1
                    direction=1
                elif col==0:
                    row+=1
                    direction=1
                else:
                    row+=1
                    col-=1
                

        return result
            