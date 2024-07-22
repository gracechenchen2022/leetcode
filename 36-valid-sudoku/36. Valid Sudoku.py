class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # 使用字典来保存行、列和小格子中的数字
        rows = [{} for _ in range(9)]
        columns = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3
                    
                    # 检查这个数字在当前行是否已经出现过
                    rows[i][num] = rows[i].get(num, 0) + 1
                    # 检查这个数字在当前列是否已经出现过
                    columns[j][num] = columns[j].get(num, 0) + 1
                    # 检查这个数字在当前3x3小格子中是否已经出现过
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                    
                    # 如果当前数字在行、列或3x3小格子中已经出现过不止一次，数独无效
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
                    
        return True
