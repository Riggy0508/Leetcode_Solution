// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hash1={}
        
        
        for num in nums:
            if num not in hash1:
                hash1[num]=1
            else:
                hash1[num]+=1
                
        res=[]
        for i in range(1,len(nums)+1):
            if i not in hash1:
                res.append(i)
        return res