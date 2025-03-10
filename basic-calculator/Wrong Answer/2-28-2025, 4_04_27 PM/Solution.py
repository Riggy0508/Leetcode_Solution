// https://leetcode.com/problems/basic-calculator

class Solution:
    def calculate(self, s: str) -> int:

        def evaluate(stack):
            res=0
            sign=1
            while stack:
                top=stack.pop()
                if top =="(":
                    break
                res+=top*sign

            if stack and isinstance(stack[-1],int):
                res*=stack.pop()

            return res
        stack=[]
        num=0
        sign=1

        for i,val in enumerate(s):
            if val.isdigit():
                num=num*10+int(val)
            
            if val in "+-(" or i==len(s)-1 or val==")":
                stack.append(num*sign)
                num=0

                if val == "+":
                    sign=1
                elif val=="-":
                    sign=-1
                elif val=="(":
                    stack.append(sign)
                    stack.append("(")

                else:
                    stack.append(evaluate(stack))

        return sum(stack)
