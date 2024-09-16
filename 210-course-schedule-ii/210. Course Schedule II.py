class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(numCourses)]
        for course, preq in prerequisites:
            graph[preq].append(course)
        state = [0] * numCourses
        result = []
        self.is_possible = True
        def dfs(course):
            if state[course] == 1:
                self.is_possible = False
                return
            if state[course] == 2:
                return
            state[course] = 1
            for next_course in graph[course]:
                if self.is_possible:
                    dfs(next_course)
            state[course] = 2
            result.append(course)
        for i in range(numCourses):
            if self.is_possible and state[i] == 0:
                dfs(i)
        return result[::-1] if self.is_possible else []