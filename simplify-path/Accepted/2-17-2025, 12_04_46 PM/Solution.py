// https://leetcode.com/problems/simplify-path

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]

        for c in path.split("/"):
            if c =="..":
                if stack:
                    stack.pop()

            else:
                if c not in ("","."):
                    stack.append(c)


        return "/"+"/".join(stack)
