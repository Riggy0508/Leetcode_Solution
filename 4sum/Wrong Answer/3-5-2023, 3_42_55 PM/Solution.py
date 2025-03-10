// https://leetcode.com/problems/4sum

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        Fans=[]
        
        
        def kSum(target,k,start):
            if k!=2:
                for i in range(start,len(nums)-k+1):
                    if i>0 and nums[i]==nums[i-1]:
                        continue
                    res.append(nums[i])
                    kSum(target-nums[i],k-1,i+1)
                    res.pop()
                    
                l=start+1
                r=len(nums)-1
                while l<r:
                    if nums[l]+nums[r]<target:
                        l+=1
                    elif nums[l]+nums[r]>target:
                        r-=1
                    else:
                        Fans.append(res+[nums[r],nums[l]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
        kSum(target,4,0)
        return Fans