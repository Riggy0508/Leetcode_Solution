// https://leetcode.com/problems/divide-two-integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        max1=2**31-1
        min1=-2**31
        negative=False
        quotient=0

        if dividend==min1 and divisor==-1:
            return max1

        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
            negative=True
        
        up=abs(dividend)
        down=abs(divisor)

        while up>=down:
            temp=down
            multiple=1
            while up>=temp+temp:
                temp=temp+temp
                multiple=multiple+multiple
            up-=temp
            quotient+=multiple

        return -quotient if negative else quotient 
