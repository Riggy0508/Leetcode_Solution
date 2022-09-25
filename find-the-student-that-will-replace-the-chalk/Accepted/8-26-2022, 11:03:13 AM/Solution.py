// https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s=sum(chalk)
        round=k//s
        chalk_needed=round*s
        k=k-chalk_needed
        
        for i in range(len(chalk)):
            if k-chalk[i]<0:
                return i
            k=k-chalk[i]
        