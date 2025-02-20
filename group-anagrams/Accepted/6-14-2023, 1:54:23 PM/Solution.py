// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash1=collections.defaultdict(list)
        res=[]

        for st in strs:
            sorted_w="".join(sorted(st))
            hash1[sorted_w].append(st)
        
        for i in hash1:
            res.append(hash1[i])
        
        return res