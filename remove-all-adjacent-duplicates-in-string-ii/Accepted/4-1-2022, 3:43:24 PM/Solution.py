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
            
        #return stack
        result = ""  
        for i in range(0, len(stack)):
            element = stack.pop()
            repeat = element[1]
            for i in range(repeat):
                temp = element[0]
                temp += result
                result = temp
        return result