// https://leetcode.com/problems/subarray-sum-equals-k

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash1={0:1}
        prefix_sum=0
        count=0


        for num in nums:
            prefix_sum+=num

            if prefix_sum-k in hash1:
                count+=hash1[prefix_sum-k]

            hash1[prefix_sum]=hash1.get(prefix_sum,0)+1

        return count