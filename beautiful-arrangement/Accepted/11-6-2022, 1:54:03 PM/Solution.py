// https://leetcode.com/problems/beautiful-arrangement

class Solution:
    def countArrangement(self, n: int) -> int:
        
        self.count=0
        nums=[]
        for i in range(1,n+1):
            nums.append(i)
        
        def dfs(nums,i:int=1):
            if i==n+1:
                self.count+=1
                return
            
            for j,val in enumerate(nums):
                #print(j,val)
                if not(val % i and i % val):
                    dfs(nums[:j]+nums[j+1:],i+1)
    
    
        dfs(nums)
        return self.count
        
        
        
        
        
        
        
        