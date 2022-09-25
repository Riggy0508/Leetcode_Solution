// https://leetcode.com/problems/reshape-the-matrix

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n,m=len(mat[0]),len(mat)
        t=r*c
        if n*m!=t: return mat
        
        output=[[0 for _ in range(c)] for _ in range(r)]
        tmp=[]
        for i in range(m):
            for j in range(n):
               tmp.append(mat[i][j])
        k=0
        for i in range(r):
            for j in range(c):
                output[i][j]=tmp[k]
                k+=1
        return output
    