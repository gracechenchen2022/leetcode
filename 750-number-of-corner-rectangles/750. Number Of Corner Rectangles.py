class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0 

        for i in range(rows):
            for j in range(i + 1, rows):
                bitwise_and_result = 0 
                same_col_count = 0
                for col in range(cols):
                    if grid[i][col] == 1 and grid[j][col] == 1:
                        same_col_count += 1

                if same_col_count > 1:
                    count += same_col_count * (same_col_count - 1)//2
        return count