// https://leetcode.com/problems/count-primes

class Solution:
    def countPrimes(self, n: int) -> int:
        # we do know that 0 and 1 are not prime numbers
        
        if n==0 or n==1: return 0
        primes=[1]*n
        
        primes[0]=0
        primes[1]=0
        
        i=2
        while i<n:
            temp=i
            if primes[i]:
                temp+=i
                while temp<n:
                    primes[temp]=0
                    temp+=i
            i+=1
            
        return sum(primes)