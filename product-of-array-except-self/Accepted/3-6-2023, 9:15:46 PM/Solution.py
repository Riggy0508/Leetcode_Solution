// https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        leftArray=[0]*n
        rightArray=[0]*n
        ans=[0]*n
        
        leftArray[0]=1
        rightArray[len(nums)-1]=1
        
        for i in range(1,len(nums)):
            leftArray[i]=leftArray[i-1]*nums[i-1]
            
        for i in reversed(range(n-1)):
            rightArray[i]=rightArray[i+1]*nums[i+1]
            
            
        for i in range(n):
            ans[i]=leftArray[i]*rightArray[i]
            
        return ans
            
            
        