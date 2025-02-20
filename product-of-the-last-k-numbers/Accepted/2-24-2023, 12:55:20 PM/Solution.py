// https://leetcode.com/problems/product-of-the-last-k-numbers

class ProductOfNumbers:

    def __init__(self):
        self.array=[1]
        

    def add(self, num: int) -> None:
        if num==0:
            self.array=[1]
        else:
            self.array.append(self.array[-1]*num)

    def getProduct(self, k: int) -> int:
        if k>=len(self.array): return 0
        return self.array[-1]//self.array[-k-1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)