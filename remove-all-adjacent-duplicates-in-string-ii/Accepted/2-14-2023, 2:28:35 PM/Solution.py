// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]

        for i in s:
            if stack and stack[-1][0]==i:
                stack[-1][1]+=1
            else:
                stack.append([i,1])
            if stack[-1][1]==k:
                stack.pop()

        return "".join(i*n for i,n in stack)



        stack=[]

        for c in s:
            if stack and stack[-1][0]==c:
                stack[-1][1]+=1
            else:
                stack.append([c,1])
            if stack[-1][1]==k:
                stack.pop()
        
        
        return "".join(c*n for c,n in stack)