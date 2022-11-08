// https://leetcode.com/problems/beautiful-arrangement

class Solution:
    def countArrangement(self, n: int) -> int:
        
        #Creating my array
        myArr=[]
        
        n=3
        0 , 1, 2 
        False, False
        
        count=0
        #bool array
        arr1=[False for i in range(n)]
        for i in range(n):
            myArr.append(n)
        
        #At this stage I will have my array created and I will implement the 2 conditions
        #1. if perm[i] is divisible byi
        
        for i in range(myArr):
            if arr1[i-1] is False:
                if myArr[i]%2==0 or i % myArr[i]==0:
                    count+=1
                    
                    
        
                
        
        #[1,2]
        
        
        
        
        
            