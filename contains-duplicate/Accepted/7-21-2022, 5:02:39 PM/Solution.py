// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap={}
        
        for n in nums:
            if n in hashMap:
                return True
            else:
                hashMap[n]=1