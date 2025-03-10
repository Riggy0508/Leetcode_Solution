// https://leetcode.com/problems/design-hashmap

class MyHashMap:

    def __init__(self):
        self.l=[-1 for _ in range(1000000)]

    def put(self, key: int, value: int) -> None:
        self.l[key]=value

    def get(self, key: int) -> int:   #O(n)
        return self.l[key]

    def remove(self, key: int) -> None:
        self.l[key]=-1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)