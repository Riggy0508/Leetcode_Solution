// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string

class Solution:
    def removeDuplicates(self, s: str) -> str:
        output=[]

        for ch in s:
            if output and ch==output[-1]:
                output.pop()
            else:
                output.append(ch)

        return "".join(output)