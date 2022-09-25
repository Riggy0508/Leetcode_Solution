// https://leetcode.com/problems/search-a-2d-matrix-ii

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col=len(matrix),len(matrix[0])
        
        top,bot=0,row-1
        
        while bot>=0 and top<col:
            if matrix[bot][top]==target:
                return True
            if matrix[bot][top]<target:
                top+=1
            else:
                bot-=1
        return False