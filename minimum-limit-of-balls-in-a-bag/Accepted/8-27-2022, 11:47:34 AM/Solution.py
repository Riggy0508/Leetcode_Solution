// https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag

class Solution:
    def isValid(self,nums,maxSize,maxOperations):
        requiredOperations=0
        for num in nums:
            operation=num//maxSize
            if num%maxSize==0:
                operation-=1
            requiredOperations+=operation
        return requiredOperations<=maxOperations
    
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        minPenalty,maxPenalty=1,max(nums)
        while minPenalty<maxPenalty:
            mid=minPenalty+((maxPenalty-minPenalty)//2)
            if self.isValid(nums,mid,maxOperations):
                maxPenalty=mid
            else:
                minPenalty=mid+1
        return maxPenalty
                
        