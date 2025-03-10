// https://leetcode.com/problems/flood-fill

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        R,C=len(image),len(image[0])
        newColor=image[sr][sc]
        if newColor==color:
            return image
        
        def dfs(r,c):
            if image[r][c]==newColor:
                image[r][c]=color
                if r>=1:
                    dfs(r-1,c)
                if R>r+1:
                    dfs(r+1,c)
                if c>=1:
                    dfs(r,c-1)
                if C>c+1:
                    dfs(r,c+1)
                
        dfs(sr,sc)
        return image
        