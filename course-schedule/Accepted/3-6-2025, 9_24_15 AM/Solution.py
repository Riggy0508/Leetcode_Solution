// https://leetcode.com/problems/course-schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph=defaultdict(list)

        for course,prereq in prerequisites:
            graph[prereq].append(course)

        visited=[0]*numCourses

        def dfs(course):
            if visited[course]==2:
                return True

            if visited[course]==1:
                return False

            visited[course]=1

            for nextCourse in graph[course]:
                if not dfs(nextCourse):
                    return False

            visited[course]=2
            return True

        for course in range(numCourses):
            if visited[course]==0:
                if not dfs(course):
                    return False

        return True