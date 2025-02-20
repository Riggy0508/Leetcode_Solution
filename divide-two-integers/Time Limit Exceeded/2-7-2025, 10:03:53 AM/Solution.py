// https://leetcode.com/problems/divide-two-integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        max1=2**31-1 
        min1=-2**31

        if dividend==min1 and divisor==-1:
            return max1

        negative=False
        up=abs(dividend)
        down=abs(divisor)
        quotient=0

        if (dividend < 0 and divisor>0) or (dividend >0 and divisor<0):
            negative=True

        while up>=down:
            up-=down
            quotient+=1

        return -quotient if negative else quotient