// https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        
        for i in word1:
            if abs(word1.count(i)-word2.count(i))>3:
                return False

        for j in word2:
            if abs(word1.count(j)-word2.count(j))>3:
                return False
        
        return True