// https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort(key=lambda x:x[0])
        # merged=[]
        # for interval in intervals:
        #     if not merged or merged[-1][1]<interval[0]:
        #         merged.append(interval)
        #     else:
        #         merged[-1][1]=max(merged[-1][1],interval[1])
        # return merged

        intervals.sort()
        mergered=[]

        for interval in intervals:
            if not mergered or mergered[-1][1]<interval[0]:
                mergered.append(interval)
            else:
                mergered[-1][1]=max(mergered[-1][1],interval[1])
        
        return mergered
            
