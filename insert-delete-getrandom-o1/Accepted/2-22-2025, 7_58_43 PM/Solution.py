// https://leetcode.com/problems/insert-delete-getrandom-o1

class RandomizedSet:

    def __init__(self):
        self.hash1={}
        self.nums=[]

    def insert(self, val: int) -> bool:
        if val in self.hash1:
            return False
        self.hash1[val]=len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash1:
            return False
        index=self.hash1[val]
        last=self.nums[-1]
        self.nums[index]=last
        self.hash1[last]=index

        del self.hash1[val]
        self.nums.pop()
        
        return True
    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()