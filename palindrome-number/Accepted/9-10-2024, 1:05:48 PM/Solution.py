// https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        div=1
        while x>div*10:
            div*=10
        
        while x:
            left=x//div
            print(left)
            right=x%10
            print(right)

            if left!=right:
                return False
            x=(x%div)//10
            div=div/100

        return 5