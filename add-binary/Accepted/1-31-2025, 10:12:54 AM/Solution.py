// https://leetcode.com/problems/add-binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry=0
        res=""

        a,b=a[::-1],b[::-1]

        for i in range(max(len(a),len(b))):
            digitA=ord(a[i])-ord("0") if i<len(a) else 0
            digitB=ord(b[i])-ord("0") if i<len(b) else 0

            total=digitA+digitB+carry
            sum1=str(total%2)
            res=sum1+res
            carry=total//2

        if carry:
            res="1"+res
        return res
