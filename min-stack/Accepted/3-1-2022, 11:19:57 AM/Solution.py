// https://leetcode.com/problems/min-stack

class MinStack:

    def __init__(self):
        self.items=[]
        self.min_item=[]

    def push(self, val: int):
        self.items.append(val);
        val=min(val,self.min_item[-1] if self.min_item else val)
        self.min_item.append(val)

    def pop(self):
        self.items.pop();
        self.min_item.pop();

    def top(self):
        return self.items[-1];
        

    def getMin(self) -> int:
        return self.min_item[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()