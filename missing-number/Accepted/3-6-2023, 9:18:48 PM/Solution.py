// https://leetcode.com/problems/missing-number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        Expo=n*(n+1)//2
        sum1=sum(nums)

        return Expo-sum1