// https://leetcode.com/problems/to-lower-case

class Solution:
    def toLowerCase(self, s: str) -> str:
        r=""
        for str in s:
            if str.isupper():
                r+=chr(ord(str)+32)
            else:
                r+=str
        return r