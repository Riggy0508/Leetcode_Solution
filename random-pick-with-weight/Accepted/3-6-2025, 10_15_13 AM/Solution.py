// https://leetcode.com/problems/random-pick-with-weight

class Solution:

    def __init__(self, w: List[int]):
        self.prefix=[]
        prefix=0

        for weight in w:
            prefix+=weight
            self.prefix.append(prefix)
        self.total=prefix

    def pickIndex(self) -> int:
        target=self.total*random.random()

        low=0
        high=len(self.prefix)

        while low<high:
            mid=(low+high)//2
            
            if self.prefix[mid]>target:
                high=mid
            else:
                low=mid+1

        return low


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()