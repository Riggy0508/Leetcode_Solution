// https://leetcode.com/problems/top-k-frequent-elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash1={}

        freq=[[] for i in range(len(nums)+1)]

        res=[]

        for n in nums:
            if n in hash1:
                hash1[n]+=1
            else:
                hash1[n]=1
        
        for i,n in hash1.items():
            freq[n].append(i)

        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
        