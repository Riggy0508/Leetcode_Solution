// https://leetcode.com/problems/ransom-note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine):
            return False
        
        letters=collections.Counter(magazine)

        for word in ransomNote:
            if letters[word]<=0:
                return False
            letters[word]-=1
        
        return True
