// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        for i in s:
            if not stack:
                stack.append(i)

            if i==")" and stack[-1]=="(":
                stack.pop()
            elif i=="]" and stack[-1]=="[":
                stack.pop()
            elif i=="}" and stack[-1]=="{":
                stack.pop()

        return len(stack)==0