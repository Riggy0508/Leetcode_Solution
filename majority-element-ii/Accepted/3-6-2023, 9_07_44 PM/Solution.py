// https://leetcode.com/problems/majority-element-ii

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res=[]
        N=len(nums)
        count1,count2,cand1,cand2=0,0,None,None
        
        for n in nums:
            if cand1==n:
                count1+=1
            elif cand2==n:
                count2+=1
            elif count1==0:
                cand1=n
                count1+=1
            elif count2==0:
                cand2=n
                count2+=1
            else:
                count1-=1
                count2-=1
        
        return [c for c in [cand1,cand2] if nums.count(c)>N//3]
                