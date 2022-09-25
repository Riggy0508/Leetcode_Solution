// https://leetcode.com/problems/transpose-matrix

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row=len(matrix)
        col=len(matrix[0])
        
        newMatrix=[[0 for i in range(row)] for j in range (col)]
        
        for i in range (row):
            for j in range(col):
                newMatrix[j][i]=matrix[i][j]
                
        return newMatrix