

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # 用来存储柱子的索引
        max_area = 0
        heights.append(0)  # 在末尾添加一个高度为0的柱子，确保所有柱子都能被处理

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]  # 栈顶的高度
                w = i if not stack else i - stack[-1] - 1  # 宽度计算
                max_area = max(max_area, h * w)
            stack.append(i)

        return max_area


#tc：on
#sc: on