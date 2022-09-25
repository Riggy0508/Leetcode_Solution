// https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        
        for r in range(n):
            i=n-1-r
            if digits[i]==9:
                digits[i]=0
            else:
                digits[i]+=1
                return digits
        return [1]+digits
        
        """
        n=len(digits)
        for r in range (n):
            i=n-1-r
            if digits[i]==9:
                digits[i]=0
            else:
                digits[i]+=1
                return digits
        return [1]+digits
            """