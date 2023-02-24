// https://leetcode.com/problems/snakes-and-ladders

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        length=len(board)
        board.reverse()
        # We need to reverse the board because we are not starting from bottom left corner rather than  the normal top left. Plus doing so will help us with our calculations

        def intoPos(square):
            r=(square-1)//length
            c=(square-1)%length
            if r%2:
                c=length-1-c
            return [r,c]

        q=collections.deque()
        q.append([1,0])
        visit=set()
        while q:
            square,moves= q.popleft()

            for i in range(1,7):
                nextSquare = square + i

                r,c=intoPos(nextSquare)
                if board[r][c]!=-1:
                    nextSquare=board[r][c]
                if nextSquare==length*length:
                    return moves+1
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare , moves + 1])
        return -1
