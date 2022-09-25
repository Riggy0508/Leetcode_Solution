// https://leetcode.com/problems/interval-list-intersections

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        a,b=0,0
        N,M=len(firstList),len(secondList)
        output=[]
        
        while (a<N and b<M):
            start=max(firstList[a][0],secondList[b][0])
            end=min(firstList[a][1],secondList[b][1])
            
            if start<=end:
                output.append([start,end])
            if firstList[a][1]<secondList[b][1]:
                a+=1
            else:
                b+=1
                
        return output
        