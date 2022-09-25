// https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*(len(nums))
        
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            #print(res[i])
            prefix*=nums[i]
            #print(prefix)
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            #print(res[i])
            postfix*=nums[i]
            #print(postfix)
        return res
    
    