// https://leetcode.com/problems/first-completely-painted-row-or-column

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        ROWS=len(mat)
        COLS=len(mat[0])

        mat_to_pos={}

        for r in range(ROWS):
            for c in range(COLS):
               mat_to_pos[mat[r][c]]=(r,c)

        ROWS_CNT=0*ROWS
        COLS_CNT=0*COLS

        for i in range(len(arr)):
            r,c=mat_to_pos[arr[i]]
            ROWS_CNT+=1
            COLS_CNT+=1

            if ROWS_CNT==cols or COLS_CNT==rows:
                return i 