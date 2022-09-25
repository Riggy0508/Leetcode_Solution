// https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        
        for i in range(len(strs[0])):
            for s in strs:
                print(s[i],strs[0][i])
                if i==len(s) or s[i]!=strs[0][i]:
                    print(res)
                    return res
            res+=strs[0][i]
            
        return res