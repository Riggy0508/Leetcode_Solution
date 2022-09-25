// https://leetcode.com/problems/palindrome-permutation

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        sets=set()
        
        for char in s:
            if char in sets:
                sets.remove(char)
            else:
                sets.add(char)
        return (len(sets)<=1)