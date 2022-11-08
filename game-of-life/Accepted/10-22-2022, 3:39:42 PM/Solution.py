// https://leetcode.com/problems/game-of-life

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows=len(board)
        cols=len(board[0])
        
        direction=[(1,1),(1,-1),(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1)]
        
        for i in range(rows):
            for j in range(cols):
                live_neighbors_count=0
                for dr in direction:
                    nr=(i+dr[0])
                    nc=(j+dr[1])
                    
                    if (nr>=0 and nr<rows) and (nc>=0 and nc<cols) and (board[nr][nc]==1 or board[nr][nc]==2):
                        live_neighbors_count+=1
                    #print(live_neighbors_count)
            
            
            #2==live_to_die
            #3==dead_to_alive
                if board[i][j]==1 and (live_neighbors_count<2 or live_neighbors_count>3):
                    board[i][j]=2
                if board[i][j]==0 and live_neighbors_count==3:
                    board[i][j]=3
                
                
        for i in range(rows):
            for j in range(cols):
                if board[i][j]==2:
                    board[i][j]=0
                elif board[i][j]==3:
                    board[i][j]=1
                