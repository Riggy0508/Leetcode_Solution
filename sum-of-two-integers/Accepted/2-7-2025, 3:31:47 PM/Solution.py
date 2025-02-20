// https://leetcode.com/problems/sum-of-two-integers

class Solution:
    def getSum(self, a: int, b: int) -> int:
        if b == 0:
            return a  # Base case: when b is reduced to 0, return a
        elif b > 0:
            return self.getSum(a + 1, b - 1)  # Increment a and decrement b
        else:
            return self.getSum(a - 1, b + 1)  # Decrem
        