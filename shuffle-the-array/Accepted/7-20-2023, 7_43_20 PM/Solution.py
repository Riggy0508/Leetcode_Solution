// https://leetcode.com/problems/shuffle-the-array

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        myArr=[]

        for i in range(len(nums)//2):
            myArr.append(nums[i])
            myArr.append(nums[i+n])
        
        return myArr
