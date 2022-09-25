// https://leetcode.com/problems/rotate-image

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for layer in range(n//2):
            first=layer
            last=n-layer-1
            for i in range(first,last):
                #Save the top
                top=matrix[layer][i]
                #move left element to top
                matrix[layer][i]=matrix[-i-1][layer]
                #move bottom element to left
                matrix[-i-1][layer]=matrix[-layer-1][-i-1]
                #move right to bottom
                matrix[-layer-1][-i-1]=matrix[i][-layer-1]
                #move top to right
                matrix[i][-layer-1]=top