// https://leetcode.com/problems/fizz-buzz

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def fib(i):
            if i%3==0 and i%5==0:
                return "FizzBuzz"
            elif i%3==0:
                return "Fizz"
            elif i%5==0:
                return "Buzz"
            else:
                return str(i)
            
        return [fib(i) for i in range(1,n+1)]