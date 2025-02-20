// https://leetcode.com/problems/moving-average-from-data-stream

class MovingAverage:

    def __init__(self, size: int):
        self.size=size
        self.q=deque()
        self.cur_sum=0


    def next(self, val: int) -> float:
        self.q.append(val)
        self.cur_sum+=val

        if len(self.q)>self.size:
            oldest=self.q.popleft()
            self.cur_sum-=oldest

        return self.cur_sum/len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)