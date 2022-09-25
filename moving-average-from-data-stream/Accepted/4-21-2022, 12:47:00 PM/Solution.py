// https://leetcode.com/problems/moving-average-from-data-stream

class MovingAverage:

    def __init__(self, size: int):
        self.queue=[]
        self.size=size

    def next(self, val: int) -> float:
        size,queue=self.size,self.queue
        queue.append(val)
        #print(queue[-3:])
        window_sum=sum(queue[-size:])
        
        return window_sum/min(len(queue),size)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)