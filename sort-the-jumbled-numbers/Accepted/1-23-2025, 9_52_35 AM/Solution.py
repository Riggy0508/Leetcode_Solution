// https://leetcode.com/problems/sort-the-jumbled-numbers

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairs=[]

        for i,num in enumerate(nums):
            num=str(num)
            map1=0
            for digit in num:
                map1*=10
                map1+=mapping[int(digit)]
            pairs.append((map1,i))

        pairs.sort()

        return [nums[p[1]] for p in pairs]