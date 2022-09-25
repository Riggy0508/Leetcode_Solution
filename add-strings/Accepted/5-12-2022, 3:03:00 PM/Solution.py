// https://leetcode.com/problems/add-strings

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m,n=len(num1),len(num2)
        a,b=m-1,n-1
        carry=0
        output=""
        while a>=0 or b>=0:
            i,j=0,0
            if a>=0:
                i=ord(num1[a])-48
                a-=1
            if b>=0:
                j=ord(num2[b])-48
                b-=1
            temp=i+j+carry
            if temp>9:
                carry=1
            else:
                carry=0
            output=str(temp)[-1]+output
        if carry:
            output="1"+output
        return output