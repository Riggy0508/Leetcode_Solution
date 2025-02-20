// https://leetcode.com/problems/moving-average-from-data-stream

class MovingAverage:

    def __init__(self, size: int):
        self.size=size
        self.queue=[]

    def next(self, val: int) -> float:
        self.queue.append(val)

        window_sum=sum(self.queue[-self.size:])
        print(window_sum)

        return window_sum/min(len(self.queue),self.size)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)