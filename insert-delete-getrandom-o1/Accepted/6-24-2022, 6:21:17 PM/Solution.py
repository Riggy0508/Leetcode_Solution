// https://leetcode.com/problems/insert-delete-getrandom-o1

class RandomizedSet:

    def __init__(self):
        self.dict={}
        self.list=[]

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val]=len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            last_element,idx=self.list[-1],self.dict[val]
            self.list[idx],self.dict[last_element]=last_element,idx            
            self.list.pop()
            del self.dict[val]
            return True

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()