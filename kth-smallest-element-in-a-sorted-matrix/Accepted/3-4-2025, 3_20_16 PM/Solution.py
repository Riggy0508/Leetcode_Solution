// https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        left,right=matrix[0][0],matrix[n-1][n-1]



        def missingCount(mid):
            row=n-1
            col=0
            count=0
            while row>=0 and col<n:
                if matrix[row][col]<=mid:
                    count+=row+1
                    col+=1
                else:
                    row-=1

            return count
        while left<right:
            mid=(left+right)//2

            if missingCount(mid)<k:
                left=mid+1
            else:
                right=mid

        return left