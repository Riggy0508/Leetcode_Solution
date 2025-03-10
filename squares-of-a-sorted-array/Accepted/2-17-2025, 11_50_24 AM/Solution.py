// https://leetcode.com/problems/squares-of-a-sorted-array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[0]*n

        l,r=0,n-1

        for i in range(n-1,-1,-1):
            if abs(nums[l])<abs(nums[r]):
                square=nums[r]
                r-=1
            else:
                square=nums[l]
                l+=1

            result[i]=square*square

        return result