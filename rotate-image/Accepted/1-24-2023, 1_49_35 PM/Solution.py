// https://leetcode.com/problems/rotate-image

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l,r=0,len(matrix)-1
        while l<r:
            for i in range(r-l):
                top,bottom=l,r

                #Save topleft value
                topleft=matrix[top][l+i]

                #bottomleft to topleft
                matrix[top][l+i]=matrix[bottom-i][l]

                #botttom right to bottom left
                matrix[bottom-i][l]=matrix[bottom][r-i]

                #topright to bottom right
                matrix[bottom][r-i]=matrix[top+i][r]

                #top left to top right
                matrix[top+i][r]=topleft

            r-=1
            l+=1