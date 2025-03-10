// https://leetcode.com/problems/first-completely-painted-row-or-column

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows,cols=len(mat),len(mat[0])

        mat_to_pos={}

        for r in range(rows):
            for c in range(cols):
                mat_to_pos[mat[r][c]]=(r,c)


        rowCNT,colCNT=[0]*rows,[0]*cols

        for i in range(len(arr)):
            r,c=mat_to_pos[arr[i]]
            rowCNT[r]+=1
            colCNT[c]+=1
            if rowCNT[r]==cols or colCNT[c]==rows:
                return i