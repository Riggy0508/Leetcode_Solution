// https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        hash_set={}

        for i in arr:
            n=bin(i).count("1")
            if n in hash_set:
                hash_set[n].append(i)
            else:
                hash_set[n]=[i]
        k=sorted(hash_set.keys())
        ans=[]
        for i in k:
            ans.extend(sorted(hash_set[i]))
        return ans