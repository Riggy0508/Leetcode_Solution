// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        output=[]
        if len(digits)==0:
            return []
        
        
        def backtrack(index=0,path=[]):
            if len(path)==len(digits):
                output.append("".join(path.copy()))
                return
            
            
            combo=letters[digits[index]] #ABC
            
            for i in combo:
                path.append(i)
                backtrack(index+1,path)
                path.pop()
        
        
    
        
        backtrack()
        return output
    