// https://leetcode.com/problems/custom-sort-string

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        char_counter=Counter(s)
        result=[]

        for char in order:
            if char in char_counter:
                result.append(char*char_counter[char])

            del char_counter[char]


        for char,count in char_counter.items():
            result.append(char*count)

        return "".join(result)