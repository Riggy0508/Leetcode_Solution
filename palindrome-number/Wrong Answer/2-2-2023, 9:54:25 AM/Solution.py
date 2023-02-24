// https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        div=1
        while x>10*div:
            div*=10
        print(div)