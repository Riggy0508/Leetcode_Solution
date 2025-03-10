// https://leetcode.com/problems/walls-and-gates

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        
        rows,cols=len(rooms),len(rooms[0])
        q=deque()

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c]==0:
                    q.append((r,c))

        direction=[(-1,0),(1,0),(0,-1),(0,1)]


        while q:
            r,c=q.popleft()

            for dr,dc in direction:
                nr,nc=dr+r,dc+c
                if 0<=nr<rows and 0<=nc<cols and rooms[nr][nc]==2147483647:
                    rooms[nr][nc]=rooms[r][c]+1
                    q.append((nr,nc))