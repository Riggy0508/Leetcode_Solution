// https://leetcode.com/problems/beautiful-arrangement

class Solution:
    def countArrangement(self, n: int) -> int:
        
        #Create our array from the value of n, we are using 1 till n+1 
        nums=[i for i in range(1,n+1)]
        
        #Count variable.
        self.count=0
        
        def dfs(nums,i:int=1):
            #base condition, we need to increase the count when we have come to an end
            if i==n+1:
                self.count+=1
                return
            
            
            #checking for the 2 conditions, and changing our array
            
            for j,val in enumerate(nums):
                #what we are basically doing is we are trying to reduce the size of the array if a current value doesn't satisfy the condition
                if not (val%i and i% val):
                    dfs(nums[:j]+nums[j+1:],i+1)
        
        dfs(nums)
        return self.count
        