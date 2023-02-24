// https://leetcode.com/problems/course-schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preDic={i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            preDic[crs].append(pre)
        
        print(preDic)