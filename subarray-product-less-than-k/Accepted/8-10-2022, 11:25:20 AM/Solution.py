// https://leetcode.com/problems/subarray-product-less-than-k

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        N=len(nums)
        product_so_far=1
        mini=0
        subarrays=0
        total=0
        
        
        for i in range(N):
            product_so_far*=nums[i]
            subarrays+=1
            
            
            while product_so_far>=k and mini<=i:
                product_so_far/=nums[mini]
                mini+=1
                subarrays-=1
                
            if product_so_far<k:
                total+=subarrays
                
        return total