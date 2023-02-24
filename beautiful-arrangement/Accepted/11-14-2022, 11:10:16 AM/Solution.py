// https://leetcode.com/problems/beautiful-arrangement

class Solution:
    def countArrangement(self, n: int) -> int:
        
        
        
        def backtrack(i=1,visited=set()):
            if len(visited)==n:
                return 1
            
            total=0
            
            for j in range(1,n+1):
                if j in visited:
                    continue
                if j%i==0 or i%j==0:
                    visited.add(j)
                    total+=backtrack(i+1,visited)
                    visited.remove(j)
                                        
            return total

        return backtrack()