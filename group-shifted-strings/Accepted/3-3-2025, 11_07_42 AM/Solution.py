// https://leetcode.com/problems/group-shifted-strings

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        if not strings:
            return []


        def getString(s):
            if not s:
                return
            
            ans=[]
            for i in range(1,len(s)):
                key=(ord(s[i])-ord(s[i-1]))%26
                ans.append(key)

            return tuple(ans)


        hash1=defaultdict(list)

        for s in strings:
            hash1[getString(s)].append(s)

        return list(hash1.values())