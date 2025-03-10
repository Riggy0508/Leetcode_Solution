// https://leetcode.com/problems/moving-average-from-data-stream

class MovingAverage:

    def __init__(self, size: int):
        self.size=size
        self.stream=deque()
        self.sum=0

    def next(self, val: int) -> float:
        self.sum+=val
        self.stream.append(val)

        if len(self.stream)>self.size:
            self.sum-=self.stream.popleft()

        return self.sum/len(self.stream)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)