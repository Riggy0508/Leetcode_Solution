// https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remove=set()
        result=[]
        stack=[]

        for i,val in enumerate(s):
            if val =="(":
                stack.append(i)

            elif val==")":
                if stack:
                    stack.pop()
                else:
                    remove.add(i)

        for index in stack:
            remove.add(index)

        for i,val in enumerate(s):
            if i not in remove:
                result.append(val)


        return result