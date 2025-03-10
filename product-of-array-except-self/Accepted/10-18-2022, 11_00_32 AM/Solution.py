// https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        
        leftArray=[0]*length
        rightArray=[0]*length
        ans=[0]*length
        
        leftArray[0]=1
        
        for i in range(1,length):
            leftArray[i]=leftArray[i-1]*nums[i-1]
        
        rightArray[length-1]=1
        for i in reversed(range(length-1)):
            rightArray[i]=rightArray[i+1]*nums[i+1]
        
        for i in range(length):
            ans[i]=leftArray[i]*rightArray[i]
        
        return ans