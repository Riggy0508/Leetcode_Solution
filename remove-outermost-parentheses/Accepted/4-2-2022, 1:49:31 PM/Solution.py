// https://leetcode.com/problems/remove-outermost-parentheses

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        stack=[]
        res=""
        
        for i in range(len(s)):
            cur_el=s[i]
            if len(stack)==0 and cur_el=="(":
                stack.append(cur_el)
            else:
                if cur_el=="(":
                    stack.append(cur_el)
                    res+=cur_el
                else:
                    stack.pop()
                    
                    if len(stack)!=0:
                        res+=cur_el
        return res
                