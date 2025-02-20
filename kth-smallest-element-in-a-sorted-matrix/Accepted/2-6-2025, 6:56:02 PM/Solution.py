// https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)

        low=matrix[0][0]
        high=matrix[n-1][n-1]

        def countLessEqual(mid):
            count=0
            row=n-1
            col=0
            while row>=0 and col<n:
                if matrix[row][col]<=mid:
                    count+=(row+1)
                    col+=1
                else:
                    row-=1
            return count

        while low<high:
            mid=(low+high)//2

            if countLessEqual(mid)<k:
                low=mid+1
            else:
                high=mid

        return high