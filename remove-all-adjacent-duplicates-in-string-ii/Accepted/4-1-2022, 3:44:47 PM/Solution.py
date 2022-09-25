// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        
        for char in s:
            if stack and stack[-1][0]==char:
                stack[-1][1]+=1
            else:
                stack.append([char,1])
            if stack and stack[-1][1]==k:
                stack.pop()
        return "".join([c*n for c,n in stack])