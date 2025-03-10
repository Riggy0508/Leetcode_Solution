// https://leetcode.com/problems/jewels-and-stones

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel=set(jewels)
        count=0

        for stone in stones:
            if stone in jewel:
                count+=1
        
        return count