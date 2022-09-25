// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a={}
        for i in nums:
            if i in a:
                return True
            else:
                a[i]=1
        return False
        