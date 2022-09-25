// https://leetcode.com/problems/backspace-string-compare

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def hash1(r):
            stack=[]
            for si in r:
                if si!="#":
                    stack.append(si)
                elif stack:
                    stack.pop()
            return "".join(stack)
        return hash1(s)==hash1(t)