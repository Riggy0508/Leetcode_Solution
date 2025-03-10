// https://leetcode.com/problems/continuous-subarray-sum

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix={0:-1}

        prefix_sum=0

        for i,val in enumerate(nums):
            prefix_sum+=val

            remainder=prefix_sum%k

            # if remainder<0:
            #     remainder+=k 
            if remainder in prefix:
                if i-prefix[remainder]>1:
                    return True
                
            else:
                prefix[remainder]=i

        return False

    