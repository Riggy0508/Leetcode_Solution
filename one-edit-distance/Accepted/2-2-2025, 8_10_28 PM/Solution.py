// https://leetcode.com/problems/one-edit-distance

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m,n=len(s),len(t)

        if abs(m-n)>1:
            return False

        if m>n:
            return self.isOneEditDistance(t,s)

        for i in range(m):
            if s[i]!=t[i]:
                if m==n:
                    return s[i+1:]==t[i+1:]
                else:
                    return s[i:]==t[i+1:]

        return m+1==n