class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 构建邻接表表示图
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        # 状态数组，0表示未访问，1表示正在访问，2表示已访问完
        state = [0] * numCourses
        result = []
        self.is_possible = True  # 初始化为 True，表示当前没有发现环
        
        # 深度优先搜索
        def dfs(course):
            if state[course] == 1:  # 如果遇到正在访问的节点，说明有环
                self.is_possible = False  # 检测到环，设置为 False
                return
            if state[course] == 2:  # 如果节点已经处理过，直接返回
                return
            
            state[course] = 1  # 标记为正在访问
            for next_course in graph[course]:
                if self.is_possible:  # 仅当没有发现环时才继续搜索
                    dfs(next_course)
            
            state[course] = 2  # 标记为已访问完毕
            result.append(course)  # 将课程加入结果
        
        # 遍历每个课程，进行 DFS
        for i in range(numCourses):
            if self.is_possible and state[i] == 0:  # 仅当没有发现环时继续
                dfs(i)
        
        # 如果发现环，返回空数组，否则返回课程顺序
        return result[::-1] if self.is_possible else []
