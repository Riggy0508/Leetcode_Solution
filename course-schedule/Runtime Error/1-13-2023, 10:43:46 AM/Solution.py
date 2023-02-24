// https://leetcode.com/problems/course-schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preDic={i:[] for i in range(numCourses)}
        print(preDic)

        for crs,pre in prerequisites:
            preDic[crs].append(pre)
        
        visited=set()





        for crs in prerequisites:
            if not dfs(crs):
                return False
        

        return True