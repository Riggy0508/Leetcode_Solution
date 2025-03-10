// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        ans=collections.defaultdict(list)

        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord("c")]+=1
            ans[tuple(count)].append(s)
        return ans.values()