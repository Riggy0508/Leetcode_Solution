// https://leetcode.com/problems/lru-cache

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.hash1=OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.hash1:
            return -1
        self.hash1.move_to_end(key)
        return self.hash1[key]

    def put(self, key: int, value: int) -> None:
        self.hash1[key]=value
        self.hash1.move_to_end(key)

        if len(self.hash1)>self.capacity:
            self.hash1.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)