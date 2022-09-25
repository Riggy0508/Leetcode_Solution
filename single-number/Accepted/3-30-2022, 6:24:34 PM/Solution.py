// https://leetcode.com/problems/single-number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashMap={}
        for i in nums:
            if i not in hashMap:
                hashMap[i]=1
            else:
                del hashMap[i]
        
        return list(hashMap.keys())[0]
        
        