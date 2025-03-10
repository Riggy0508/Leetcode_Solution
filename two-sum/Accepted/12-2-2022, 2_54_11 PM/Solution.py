// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1={}
        
        for j,val in enumerate(nums):
            diff=target-val
            
            if diff in hash1:
                return [j,hash1[diff]]
                
            else:
                hash1[val]=j