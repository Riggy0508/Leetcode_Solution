// https://leetcode.com/problems/valid-perfect-square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r=1,num
        while l<=r:
            mid=(l+r)//2
            if mid*mid>num:
                r=r-1
            elif mid*mid<num:
                l=l+1
            else:
                return True