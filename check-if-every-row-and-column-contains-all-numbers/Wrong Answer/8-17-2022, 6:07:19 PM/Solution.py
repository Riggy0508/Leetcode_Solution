// https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])

        for r in range(rows):    
            rSet=set()
            cSet=set()
            for c in range(cols):
                if matrix[r][c] in rSet or matrix[r][c] in cSet:
                    return False
                cSet.add(matrix[r][c])
                rSet.add(matrix[r][c])
                
        return True