// https://leetcode.com/problems/backspace-string-compare

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def has2(r):
            stack=[]
            
            for s in r:
                if s!="#":
                    stack.append(s)
                elif stack:
                    stack.pop()
            return "".join(stack)
        return has2(s)==has2(t)
        
        
        
        