// https://leetcode.com/problems/append-k-integers-with-minimal-sum

class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        ans_val=k*(k+1)/2
        next_val=k+1
        nums.sort()
        
        
        for i,num in enumerate(nums):
            if i and num==nums[i-1]:
                continue
            if num>k:
                break
            else:
                ans_val=ans_val-num+next_val
                k+=1
                next_val+=1
        return int(ans_val)