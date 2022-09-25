// https://leetcode.com/problems/search-a-2d-matrix-ii

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col=len(matrix),len(matrix[0])
        #print(col)
        top,bot=0,row-1
        print(matrix[top][bot])
        while top<col and bot>=0:
            if matrix[top][bot]==target:
                return True
            if matrix[top][bot]>target:
                bot-=1
            else:
                top+=1
        return False
                
            
            
            
            
        
        
        
        
        