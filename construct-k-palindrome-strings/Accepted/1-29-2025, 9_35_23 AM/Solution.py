// https://leetcode.com/problems/construct-k-palindrome-strings

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        
        count=Counter(s)
        odd=0
        for cnt in count.values():
            odd+=cnt%2

        if odd>k:
            return False
        return True