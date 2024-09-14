from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c,0))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        if fresh_oranges == 0:
            return 0
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        minutes_passed = 0
        while queue:
            r, c, minutes = queue.popleft()
            minutes_passed = minutes
            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if 0<= nr < rows and 0<= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_oranges -= 1
                    queue.append((nr, nc, minutes+1))
        return minutes_passed if fresh_oranges == 0 else -1

