// https://leetcode.com/problems/find-missing-and-repeated-values

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        hash1={}
        repeated=0
        n=len(grid)
        total=0


        for row in grid:
            for num in row:
                total+=num
                if num in hash1:
                    repeated=num
                hash1[num]=1

        
        sum1 = n * n * ((n * n) + 1) // 2
        missing=sum1-(total-repeated)


        return [repeated,missing]