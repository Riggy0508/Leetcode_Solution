// https://leetcode.com/problems/last-stone-weight

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def remove_largest():
            index_lar=stones.index(max(stones))
            
            stones[index_lar],stones[-1]=stones[-1],stones[index_lar]
            return stones.pop()
        while len(stones)>1:
            stones_1=remove_largest()
            stones_2=remove_largest()
            
            if stones_1!=stones_2:
                stones.append(stones_1-stones_2)
            
        return stones[0] if stones else 0