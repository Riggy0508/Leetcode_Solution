// https://leetcode.com/problems/paint-house

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        print(len(costs))
        
        def paint_cost(n,color):
            if (n,color) in self.done:
                return self.done[(n,color)]
            total_cost=costs[n][color]
            if n==len(costs)-1:
                pass
            elif color==0:
                total_cost+=min(paint_cost(n+1,1),paint_cost(n+1,2))
            elif color==1:
                total_cost+=min(paint_cost(n+1,0),paint_cost(n+1,2))
            elif color==2:
                total_cost+=min(paint_cost(n+1,0),paint_cost(n+1,1))
            
            self.done[(n,color)]=total_cost
            return total_cost
        self.done={}
        return min(paint_cost(0,0),paint_cost(0,1),paint_cost(0,2))