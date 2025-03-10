// https://leetcode.com/problems/basic-calculator-ii

class Solution:
    def calculate(self, s: str) -> int:
        current=0
        lastO="+"
        stack=[]

        for i,val in enumerate(s):
            if val.isdigit():
                current=current*10+int(val)
            
            if val in "+-*/" or i==len(s)-1:
                if lastO=="+":
                    stack.append(current)
                elif lastO=="-":
                    stack.append(-current)
                elif lastO=="*":
                    stack.append(stack.pop()*current)

                elif lastO=="/":
                    stack.append(int(stack.pop()/current))

                current=0
                lastO=val

        return sum(stack)

