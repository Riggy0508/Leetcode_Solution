// https://leetcode.com/problems/lru-cache

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.hash1={}
        

    def get(self, key: int) -> int:
        if key in has1:
            return self.hash1[key]

        

    def put(self, key: int, value: int) -> None:
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)