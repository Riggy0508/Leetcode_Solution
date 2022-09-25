// https://leetcode.com/problems/excel-sheet-column-title

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res=""
        print(columnNumber)
        while (columnNumber!=0):
            columnNumber-=1
            #print(columnNumber)
            temp=columnNumber%26
            #print(temp)
            res+=chr(65+temp)
            #print(res)
            columnNumber=columnNumber//26
            #print(columnNumber)
            
        return res[::-1]