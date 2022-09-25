// https://leetcode.com/problems/valid-triangle-number

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        output=0
        N=len(nums)
        for k in range(2,N):
            i,j=0,k-1
            while i<j:
                if nums[i]+nums[j]>nums[k]:
                    output+=(j-i)
                    j-=1
                else:
                    i+=1
        return output
        
        
            
            