// https://leetcode.com/problems/course-schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap={i:[] for i in range(numCourses)}
        #print(preMap)     {0: [], 1: []}
        for crs,pre in (prerequisites):
            preMap[crs].append(pre)
        #print(preMap)   {0: [], 1: [0]}

        
        #Creating a visit set in order to keep track of all the visited courses in order to avoid processing of it again and again
        visitSet=set()
        def dfs (crs):
            if crs in visitSet:
                return False
            if preMap[crs]==[]:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            preMap[crs]=[]
            return True
            
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True
