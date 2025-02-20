// https://leetcode.com/problems/integer-to-roman

class Solution:
    def intToRoman(self, num: int) -> str:
        list1=[["I",1],["IV",4],["V",5],["IX",9],["X",10],["XL",40],["L",50],["LC",90],["C",100],["CD",400],["D",500],["CM",900],["M",1000]]
        
        
        res=""
        
        for sys,val in reversed(list1):
            if num//val:
                count=num//val
                res+=(count*sys)
                num=num%val
        return res