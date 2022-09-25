// https://leetcode.com/problems/backspace-string-compare

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def has1(r):
            stack=[]
            
            for s in r:
                #print(s)
                if s!="#":
                    stack.append(s)
                else:
                    stack.pop()
            return "".join(stack)
                
        return has1(s)==has1(t)