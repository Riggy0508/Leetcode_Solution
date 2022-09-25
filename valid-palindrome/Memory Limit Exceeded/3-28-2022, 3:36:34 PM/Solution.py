// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        str=re.sub('[^A-Za-z0-9]+', '', s).lower()
        if len(str)==0:
            return True
        if str[0]!=str[len(str)-1]:
            return False
        return self.isPalindrome(str[1:-1])
        