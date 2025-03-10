// https://leetcode.com/problems/course-schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preDic={i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            preDic[crs].append(pre)
        
        print(preDic)
        visited=set()

        def dfs(crs):
            if crs in visited:
                return False
            if preDic[crs]==[]:
                return True

            visited.add(crs)
            for pre in preDic[crs]:
                if not dfs(pre):
                    return False

            visited.remove(crs)
            preDic[crs]=[]
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True