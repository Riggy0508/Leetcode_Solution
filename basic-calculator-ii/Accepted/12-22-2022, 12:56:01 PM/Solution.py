// https://leetcode.com/problems/basic-calculator-ii

class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        lastSign="+"
        num=0
        for i in range(len(s)):
            if s[i].isdigit():
                num=num*10+int(s[i])
            if (not s[i].isdigit()) and s[i]!=" " or i==len(s)-1:
                if lastSign=="+":
                    stack.append(num)
                if lastSign=="-":
                    stack.append(-num)
                if lastSign=="*":
                    stack.append(stack.pop()*num)
                if lastSign=="/":
                    stack.append(int(stack.pop()/num))
                lastSign=s[i]
                num=0
        
        return sum(stack)
        
                


