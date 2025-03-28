// https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            l,r=i+1,len(nums)-1

            while l<r:
                sum1=nums[i]+nums[l]+nums[r]
                if sum1>0:
                    r-=1
                elif sum1<0:
                    l+=1
                else:
                    result.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1


        return result
