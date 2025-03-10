// https://leetcode.com/problems/basic-calculator-ii

class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        num=0
        lastO="+"


        for i,val in enumerate(s):
            if val.isdigit():
                num=num*10+int(val)

            if val in "+-*/" or i==len(s)-1:

                if lastO=="+":
                    stack.append(num)
                elif lastO=="-":
                    stack.append(-num)

                elif lastO=="*":
                    stack.append(stack.pop()*num)
                
                elif lastO=="/":
                    stack.append(int(stack.pop()/num))

                num=0
                lastO=val

        return sum(stack)
