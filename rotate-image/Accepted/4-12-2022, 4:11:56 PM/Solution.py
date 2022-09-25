// https://leetcode.com/problems/rotate-image

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l,r=0,len(matrix)-1
        
        while l<r:
            top,bottom=l,r
            for i in range(r-l):
                
                topLeft=matrix[top][l+i]
                
                matrix[top][l+i]=matrix[bottom-i][l]
                
                matrix[bottom-i][l]=matrix[bottom][r-i]
                
                
                matrix[bottom][r-i]=matrix[top+i][r]
                
                matrix[top+i][r]=topLeft
                
            l+=1
            r-=1
        
        
        
        
        
        """
        Do not return anything, modify matrix in-place instead.
        
        left,right=0,len(matrix)-1
        
        while left<right:
            for i in range(right-left):
                top,bottom=left,right
                
                #save the topleft
                topLeft=matrix[top][left+i]
                
                #move bottom left to topleft
                matrix[top][left+i]=matrix[bottom-i][left]
                
                #move the bottom right to bottom left
                matrix[bottom-i][left]=matrix[bottom][right-i]
                
                #move the top right to bottom right
                matrix[bottom][right-i]=matrix[top+i][right]
                
                #move the top left to top right
                matrix[top+i][right]=topLeft
                
            left+=1
            right-=1
                """