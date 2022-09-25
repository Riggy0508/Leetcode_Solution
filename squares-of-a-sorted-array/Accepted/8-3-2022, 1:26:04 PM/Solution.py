// https://leetcode.com/problems/squares-of-a-sorted-array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        myArr=[]
        for i in range(len(nums)):
            myArr.append(nums[i]**2)
            
        myArr.sort()
        return myArr