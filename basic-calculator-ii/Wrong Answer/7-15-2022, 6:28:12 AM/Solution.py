// https://leetcode.com/problems/basic-calculator-ii

class Solution:
    def calculate(self, s: str) -> int:
        cur,prev,res=0,0,0
        cur_operation="+"
        
        i=0
        
        while i<len(s):
            cur_char=s[i]
            print(cur_char)
            
            if cur_char.isdigit():
                while i<len(s) and s[i].isdigit():
                    cur=cur*10+int(s[i])
                    i+=1
                    
                i-=1
                if cur_operation=="+":
                    res+=cur
                    
                    prev=cur
                elif cur_operation=="-":
                    res-=cur
                    
                    prev-=cur
                elif cur_operation =="*":
                    res-=prev
                    res+=prev*cur
                    
                    prev=cur*prev
                else:
                    res-=prev
                    res+=int(prev/cur)
                    
                    prev=int(prev/cur)
                    
                cur=0
            elif cur_char!=" ":
                cur_operation=cur_char
                
            i+=1
        return res