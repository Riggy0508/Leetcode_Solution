// https://leetcode.com/problems/shortest-path-in-binary-matrix

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        if grid[0][0]==1 or grid[n-1][n-1]:
            return -1

        directions=[[0,1],[0,-1],[-1,0],[1,0],[-1,-1],[-1,1],[1,-1],[1,1]]
        
        q=deque([(0,0,1)])
        grid[0][0]=1

        while q:
            r,c,distance=q.popleft()

            if r==n-1 and c==n-1:
                return distance

            for dr,dc in directions:
                r1=dr+r
                c1=dc+c
                if 0<=r1<n and 0<=c1<n and grid[r1][c1]==0:
                    q.append((r1,c1,distance+1))

                    grid[r1][c1]=1

        return distance