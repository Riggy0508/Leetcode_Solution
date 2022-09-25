// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap={}
        
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in hashMap:
                return [hashMap[diff],i]
            else:
                hashMap[nums[i]]=i
        
        
        
        
        
        
        
        
        #hashMap={}
        
        #for i in range(len(nums)):
         #   diff=target-nums[i]
          #  if diff in hashMap:
           #     return [i,hashMap[diff]]
            #hashMap[nums[i]]=i