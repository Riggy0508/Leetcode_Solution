// https://leetcode.com/problems/top-k-frequent-elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash1={}
        res=[]
        freq=[[] for i in range(len(nums)+1)]

        for i in range(len(nums)):
            hash1[nums[i]]=1+hash1.get(nums[i],0)

        for key,val in hash1.items():
            freq[val].append(key)

        
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
                
