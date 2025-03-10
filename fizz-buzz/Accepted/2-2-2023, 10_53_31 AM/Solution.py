// https://leetcode.com/problems/fizz-buzz

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans=[""]*n

        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                ans[i-1]="FizzBuzz"
            elif i%3==0:
                ans[i-1]="Fizz"
            elif i%5==0:
                ans[i-1]="Buzz"
            else:
                ans[i-1]=(str(i))
        return ans





        # def fib(i):
        #     if i%3==0 and i%5==0:
        #         return "FizzBuzz"
        #     elif i%3==0:
        #         return "Fizz"
        #     elif i%5==0:
        #         return "Buzz"
        #     else:
        #         return str(i)
            
        # return [fib(i) for i in range(1,n+1)]