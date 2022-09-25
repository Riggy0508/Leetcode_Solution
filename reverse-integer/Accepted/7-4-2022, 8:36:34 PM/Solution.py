// https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
    
        negative=x<0
        ans=0
        
        if negative:
            x=x*-1
            
        while x>0:
            rem=x%10
            ans=(ans*10)+rem
            x=x//10
            
        if negative:
            ans=ans*-1
            
        if ans>(2**31)-1 or ans<(-2)**31:
            return 0
        
        else:
            return ans
            