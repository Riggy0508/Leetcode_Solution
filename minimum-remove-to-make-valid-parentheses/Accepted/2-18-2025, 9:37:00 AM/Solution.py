// https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remove=set()
        stack=[]

        for i,c in enumerate(s):
            if c not in "()":
                continue
            if c =='(':
                stack.append(i)
            elif not stack:
                remove.add(i)
            else:
                stack.pop()
        print(stack,"|",remove)

        for index in stack:
            remove.add(index)
            
        result=[]
        for i,c in enumerate(s):
            if i not in remove:
                result.append(c)
        return "".join(result)