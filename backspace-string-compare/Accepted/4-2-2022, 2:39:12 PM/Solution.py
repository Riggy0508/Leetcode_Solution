// https://leetcode.com/problems/backspace-string-compare

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def hash1(r):
            stack1=[]
            for si in r:
                if si!='#':
                    stack1.append(si)
                elif stack1:
                    stack1.pop()
            return "".join(stack1)
        return hash1(s)==hash1(t)
        