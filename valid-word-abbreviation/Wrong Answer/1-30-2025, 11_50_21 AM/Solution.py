// https://leetcode.com/problems/valid-word-abbreviation

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i,j=0,0

        while i<len(word) and j<len(abbr):
            # if word[i]!=abbr[j]:
            #     return False

            if abbr[j].isdigit():
                num=0
                while j<len(abbr) and abbr[j].isdigit():
                    num=num*10+int(abbr[j])
                    j+=1

                i+=num
            else:
                if i>len(word) and word[i]!=abbr[j]:
                    return False
                i+=1
                j+=1
        return i==len(word) and j==len(abbr)