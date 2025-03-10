// https://leetcode.com/problems/design-a-stack-with-increment-operation

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack1=[]
        self.maxSize=maxSize
        self.stack2=[]

    def push(self, x: int) -> None:
        if len(self.stack1)<self.maxSize:
            self.stack1.append(x)
         

    def pop(self) -> int:
        if len(self.stack1)==0:
            return -1
        else:
            return self.stack1.pop()

    def increment(self, k: int, val: int) -> None:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        
        
        #-a=len(self.stack2)
        
        
        n=k
        while self.stack2:
            if n>0:
                self.stack1.append(self.stack2.pop()+val)
                n=n-1
            else:
                self.stack1.append(self.stack2.pop())
        print(self.stack1,self.stack2)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #while self.stack2:
         #   if n>0:
          #      self.stack1.append(self.stack2.pop()+val)
                #n-=1
           # else:
            #    self.stack1.append(self.stack2)
        #print(self.stack1,self.stack2)        




# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)