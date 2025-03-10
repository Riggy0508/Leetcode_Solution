// https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged=[]


        for interval in intervals:
            if merged and merged[-1][1]>=interval[0]:
                merged[-1][1]=max(merged[-1][1],interval[1])
            else:
                merged.append(interval)

        return merged