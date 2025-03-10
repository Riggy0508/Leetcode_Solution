// https://leetcode.com/problems/3sum-closest

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff=float("inf")
        nums.sort()
        
        for i in range(len(nums)):
            lo=i+1
            hi=len(nums)-1
            while lo<hi:
                sum1=nums[i]+nums[lo]+nums[hi]
                if abs(target-sum1)<abs(diff):
                    diff=target-sum1
                if sum1<target:
                    lo+=1
                else:
                    hi-=1
            if diff==0:
                break
        return target-diff
        
                