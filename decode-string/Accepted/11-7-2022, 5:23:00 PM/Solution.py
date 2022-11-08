// https://leetcode.com/problems/decode-string

class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        
        for i in range(len(s)):
            if s[i]!="]":
                stack.append(s[i])
            else:
                #if s[i]=="[" append it in the stack
                substr=""
                while stack[-1]!="[":
                    substr=stack.pop()+substr
                stack.pop()
                
                k=""
                while stack and stack[-1].isdigit():
                    k=stack.pop()+k
                
                stack.append(int(k)*substr)
                
        return "".join(stack)
                    