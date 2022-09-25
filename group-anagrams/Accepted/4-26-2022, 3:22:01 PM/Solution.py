// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        
        for c in strs:
            count=[0]*26
            for s in c:
                count[ord(s)-ord("a")]+=1
            res[tuple(count)].append(c)
        return res.values()