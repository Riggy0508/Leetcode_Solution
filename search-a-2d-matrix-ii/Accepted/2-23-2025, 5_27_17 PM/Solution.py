// https://leetcode.com/problems/search-a-2d-matrix-ii

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols=len(matrix),len(matrix[0])

        row,col=0,cols-1

        while row<rows and col>=0:
            if matrix[row][col]==target:
                return True
            if matrix[row][col]>target:
                col-=1
            else:
                row+=1
        
        return False