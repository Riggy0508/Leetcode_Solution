// https://leetcode.com/problems/course-schedule-ii

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        stack=[]
        visited=[0]*numCourses

        for course,prereqp in prerequisites:
            graph[prereqp].append(course)

        def dfs(course):
            if visited[course]==1:
                return False
            if visited[course]==2:
                return True

            visited[course]=1
            for next_course in graph[course]:
                if not dfs(next_course):
                    return False

            visited[course]=2
            stack.append(course)
            return True

        
        for course in range(numCourses):
            if visited[course]==0:
                if not dfs(course):
                    return []


        return stack[::-1]