// https://leetcode.com/problems/non-decreasing-array

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count=0
        for i in range(1, len(nums)):
            if nums[i-1]>nums[i]:
                if count==1:
                    return False
                count+=1
                
        return True