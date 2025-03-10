// https://leetcode.com/problems/letter-tile-possibilities

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(counter):
            count=0
            for s in counter:
                if counter[s]>0:
                    counter[s]-=1
                    count+=1+backtrack(counter)
                    counter[s]+=1

            return count
        return backtrack(Counter(tiles))
