class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        queue = deque([(0,0,1)])
        grid[0][0] = 1
        while queue:
            x,y,path_length = queue.popleft()
            if x == n - 1 and y == n - 1:
                return path_length
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < n and 0 <= new_y <n and grid[new_x][new_y] == 0:
                    queue.append((new_x,new_y,path_length + 1))
                    grid[new_x][new_y] = 1

        return -1
