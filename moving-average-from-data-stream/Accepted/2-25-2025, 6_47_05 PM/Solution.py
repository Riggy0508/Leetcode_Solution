// https://leetcode.com/problems/moving-average-from-data-stream

class MovingAverage:

    def __init__(self, size: int):
        self.q=deque()
        self.size=size
        self.prefix=0

    def next(self, val: int) -> float:
        self.prefix+=val
        self.q.append(val)

        if len(self.q)>self.size:
            value=self.q.popleft()
            self.prefix-=value

        return self.prefix/len(self.q)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)