// https://leetcode.com/problems/random-pick-with-weight

class Solution:

    def __init__(self, w: List[int]):
        self.prefix=[]
        self.prefixSum=0
        for weight in w:
            self.prefixSum+=weight
            self.prefix.append(self.prefixSum)

        self.total=self.prefixSum
            
    def pickIndex(self) -> int:
        target=self.total*random.random()
        print(target)

        low=0
        high=len(self.prefix)-1

        while low<high:
            mid=(low+high)//2
            if self.prefix[mid]>target:
                low=mid+1
            else:
                high=mid

        return low

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()