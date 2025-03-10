// https://leetcode.com/problems/maximum-swap

class Solution:
    def maximumSwap(self, num: int) -> int:
        nums=list(str(num))
        max_i=-1
        max_digit="0"
        a,b=-1,-1


        for i in range(len(nums)-1,-1,-1):
            if nums[i]>max_digit:
                max_digit=nums[i]
                max_i=i

            if nums[i]<max_digit:
                a,b=i,max_i

        nums[a],nums[b]=nums[b],nums[a]

        return int("".join(nums))