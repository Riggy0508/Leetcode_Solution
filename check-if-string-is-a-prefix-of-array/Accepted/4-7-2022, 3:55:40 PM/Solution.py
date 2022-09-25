// https://leetcode.com/problems/check-if-string-is-a-prefix-of-array

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        w=""
        for i in range(len(words)):
            w+=words[i]
            if len(s)==len(w):
                break
        return s==w