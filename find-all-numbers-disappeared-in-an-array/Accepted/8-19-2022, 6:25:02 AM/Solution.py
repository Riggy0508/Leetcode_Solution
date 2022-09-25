// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hash1={}
        
        for num in nums:
            hash1[num]=1
    
        res=[]
        
        for num in range(1,len(nums)+1):
            if num not in hash1:
                res.append(num)
        return res