// https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        result=1

        if n==0:
            return 1

        if n<0:
            x=1/x
            n=-n

        while n:
            if n%2==1:
                result*=x
            x*=x
            n=n//2

        return result

        