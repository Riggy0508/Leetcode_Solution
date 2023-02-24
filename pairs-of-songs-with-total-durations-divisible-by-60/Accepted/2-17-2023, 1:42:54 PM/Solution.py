// https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic=collections.defaultdict(int)

        pair=0
        for t in time:
            if t%60==0:
                pair+=dic[0]
            else:
                pair+=dic[60-t%60]
            dic[t%60]+=1
        return pair