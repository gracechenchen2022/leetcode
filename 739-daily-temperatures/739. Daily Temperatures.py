class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0]*len(T)
        stack = []
        for i, temp in enumerate(T):
            while stack and T[stack[-1]] < temp:#if max temp < current temp 30< 40
                idx = stack.pop()# 0
                res[idx] = i - idx # 1-0 = 1
            stack.append(i)
        return res
#tc:on
#sc:on