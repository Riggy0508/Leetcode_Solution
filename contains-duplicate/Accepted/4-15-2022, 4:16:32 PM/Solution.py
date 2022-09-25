// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hashMap={}
        
        for i in range(len(nums)):
            if nums[i] in hashMap:
                return True
            else:
                hashMap[nums[i]]=1
        return False
        
        """
        hashMap={}
        for i in range(len(nums)):
            if nums[i] in hashMap:
                return True
            else:
                hashMap[nums[i]]=1
        return False
                """
                