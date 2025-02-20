// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash1=collections.defaultdict(list)

        res=[]

        for s in strs:
            ss=''.join(sorted(s))
            hash1[ss].append(s)

        for i in hash1:
            res.append(hash1[i])

        return res