// https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""

        for i in range(len(strs[0])):
            for s in strs:
                if s[i]!=strs[0][i]:
                    return res
            res+=strs[0][i]
        return res
