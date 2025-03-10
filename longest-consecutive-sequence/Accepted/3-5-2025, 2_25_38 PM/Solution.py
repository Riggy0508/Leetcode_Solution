// https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        longestSequence=0

        for num in numSet:
            if num-1 not in numSet:
                current=num
                currentStreak=1
                while current+1 in numSet:
                    current+=1
                    currentStreak+=1
                
                longestSequence=max(longestSequence,currentStreak)

        return longestSequence