// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=collections.defaultdict(list)

        res=[]

        for st in strs:
            sorted_word="".join(sorted(st))
            hashmap[sorted_word].append(st)

        for i in hashmap:
            res.append(hashmap[i])
        return res