// https://leetcode.com/problems/largest-unique-number

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        hash1={}
        max1=-1
        for val in nums:
            if val in hash1:
                hash1[val]+=1
            else:
                hash1[val]=1

        
        for num,count in hash1.items():
            if count==1:
                max1=max(max1,num)
        
        return max1

