// https://leetcode.com/problems/continuous-subarray-sum

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix={0:-1}
        prefixSum=0


        for i,val in enumerate(nums):
            prefixSum+=val

            remainder=prefixSum%k

            if remainder in prefix:
                if i-prefix[remainder]>1:
                    return True
            else:
                prefix[remainder]=i

        return False