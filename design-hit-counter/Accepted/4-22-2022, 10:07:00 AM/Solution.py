// https://leetcode.com/problems/design-hit-counter

class HitCounter:

    def __init__(self):
        self.deque=collections.deque()

    def hit(self, timestamp: int) -> None:
        self.deque.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.deque and timestamp-self.deque[0]>=300:
            self.deque.popleft()
        return len(self.deque)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)