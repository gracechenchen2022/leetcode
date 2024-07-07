class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        nr = len(grid)
        nc = len(grid[0])
        num_islands = 0

        def bfs(grid, r, c):
            queue = deque([(r, c)])
            while queue:
                row, col = queue.popleft()
                for x, y in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                    if 0 <= x < nr and 0 <= y < nc and grid[x][y] == '1':
                        grid[x][y] = '0'
                        queue.append((x, y))

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    num_islands += 1
                    bfs(grid, r, c)

        return num_islands
