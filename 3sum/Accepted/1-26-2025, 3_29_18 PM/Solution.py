// https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]


        for i in range(len(nums)-1):
            if i>0 and nums[i]==nums[i-1]:
                continue

            l=i+1
            r=len(nums)-1

            while l<r:
                sum1=nums[r]+nums[l]+nums[i]
                if sum1<0:
                    l+=1
                elif sum1>0:
                    r-=1

                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        
        return res