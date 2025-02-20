// https://leetcode.com/problems/pascals-triangle-ii

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        myArr=[]

        for i in range(rowIndex+1):
            myArr.append([])
            for j in range(i+1):
                if j==0 or j==i:
                    myArr[i].append(1)
                else:
                    myArr[i].append(myArr[i-1][j-1]+myArr[i-1][j])
        
        return myArr[rowIndex]
        