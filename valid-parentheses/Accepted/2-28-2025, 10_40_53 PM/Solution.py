// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack=[]

        for p in s:
            if stack:
                if p==")" and stack[-1]=="(":
                    stack.pop()
                elif p=="]" and stack[-1]=="[":
                    stack.pop()
                elif p=="}" and stack[-1]=="{":
                    stack.pop()
                else:
                    stack.append(p)
            else:
                stack.append(p)

        return len(stack)==0
