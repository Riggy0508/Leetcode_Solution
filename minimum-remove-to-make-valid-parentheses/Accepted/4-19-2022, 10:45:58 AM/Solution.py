// https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        itr=set()
        stack=[]
        
        for i,c in enumerate(s):
            if c not in "()":
                continue
            if c=="(":
                stack.append(i)
            elif not stack:
                itr.add(i)
            else:
                stack.pop()
        itr=itr.union(set(stack))
        print(itr)
        new_string=[]
        for i,c in enumerate(s):
            if i not in itr:
                new_string.append(c)
        return "".join(new_string)