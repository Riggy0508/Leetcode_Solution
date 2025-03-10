// https://leetcode.com/problems/subarray-sum-equals-k

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix=0
        count=0
        hash1={0:1}

        for num in nums:
            prefix+=num
            if prefix-k in hash1:
                count+=hash1[prefix-k]

            hash1[prefix]=hash1.get(prefix,0)+1

        return count