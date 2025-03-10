// https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftArray=[0]*len(nums)
        rightArray=[0]*len(nums)
        ans=[0]*len(nums)

        leftArray[0]=1

        for i in range(1,len(nums)):
            leftArray[i]=leftArray[i-1]*nums[i-1]

        rightArray[len(nums)-1]=1

        for i in reversed(range(len(nums)-1)):
            rightArray[i]=rightArray[i+1]*nums[i+1]

        for i in range(len(nums)):
            ans[i]=leftArray[i]*rightArray[i]

        return ans