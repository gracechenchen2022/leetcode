class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # 从左到右遍历 top 行
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1  # top 行遍历完毕，top 往下移
            
            # 从上到下遍历 right 列
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  # right 列遍历完毕，right 往左移
            
            if top <= bottom:
                # 从右到左遍历 bottom 行
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1  # bottom 行遍历完毕，bottom 往上移
            
            if left <= right:
                # 从下到上遍历 left 列
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1  # left 列遍历完毕，left 往右移
        
        return result
