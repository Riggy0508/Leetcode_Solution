// https://leetcode.com/problems/number-of-ways-to-split-array

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        right=sum(nums)
        left=0
        
        l=len(nums)
        count=0
        
        for i,x in enumerate(nums):
            left+=x
            right-=x
            #print(i,x)
            if i+1!=l and left>=right:
                count+=1
        return count
            
        