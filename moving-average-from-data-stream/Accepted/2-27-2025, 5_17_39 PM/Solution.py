// https://leetcode.com/problems/moving-average-from-data-stream

class MovingAverage:

    def __init__(self, size: int):
        self.size=size
        self.num=[]
        self.sum=0
        

    def next(self, val: int) -> float:
        self.num.append(val)
        self.sum+=val

        if len(self.num)>self.size:
            self.sum-=self.num.pop(0)
        
        return self.sum/len(self.num)


        



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)