// https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        rows=len(grid)
        cols=len(grid[0])
        direction=[(1,0),(-1,0),(0,-1),(0,1)]

        q=collections.deque()
        steps=0
        q.append([0,0,k,steps])
        seen=set()
        seen.add((0,0,k))
        target=(rows-1,cols-1)

        while q:
            c_r,c_c,c_k,steps=q.popleft()
            if c_r==target[0] and c_c==target[1]:
                return steps

            for d in direction:
                new_r=c_r+d[0]
                new_c=c_c+d[1]

                if new_r>=0 and new_r<rows and new_c>=0 and new_c<cols:
                    k=c_k-grid[new_r][new_c]
                    if k>=0 and (new_r,new_c,k) not in seen:
                        q.append([new_r,new_c,k,steps+1])
                        seen.add((new_r,new_c,k))
        return -1



