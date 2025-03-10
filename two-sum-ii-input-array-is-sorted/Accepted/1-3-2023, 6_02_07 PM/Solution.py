// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1



        while l<r:
            sum1=numbers[l]+numbers[r]
            if sum1>target:
                r-=1
            elif sum1<target:
                l+=1
            else:
                return [l+1,r+1]