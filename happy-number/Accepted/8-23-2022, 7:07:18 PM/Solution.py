// https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:
        visit=set()
        
        while n not in visit:
            visit.add(n)
            n=self.sumS(n)
            if n==1:
                return True
        return False
    
    def sumS(self,n):
        output=0
        
        while n:
            digit1=n%10
            digit1=digit1**2
            output+=digit1
            n=n//10
        return output