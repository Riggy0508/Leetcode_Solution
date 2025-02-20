// https://leetcode.com/problems/basic-calculator-ii

class Solution:
    def calculate(self, s: str) -> int:
        lastO="+"
        current=0
        stack=[]


        for i,val in enumerate(s):
            if val.isdigit():
                current=current*10+int(s[i])
            if val in "+-*/" or i==len(s)-1:
                if lastO=="+":
                    stack.append(current)
                
                if lastO=="-":
                    stack.append(stack.pop()-current)

                if lastO=="*":
                    stack.append(stack.pop()*current)

                if lastO=="/":
                    stack.append(stack.pop()//current)

                current=0
                lastO=val

        return sum(stack)
