
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # 定义一个缓存，避免重复计算
        memo = {}

        def ways(expression, start, end):
            # 如果结果已经计算过，直接返回缓存的结果
            if (start, end) in memo:
                return memo[(start, end)]

            # 存放所有可能的结果
            res = []
            # 遍历表达式
            for i in range(start, end + 1):
                c = expression[i]
                # 如果当前字符是运算符
                if c in "+-*":
                    # 递归计算左侧和右侧的结果
                    left = ways(expression, start, i - 1)
                    right = ways(expression, i + 1, end)
                    # 组合左右两侧的结果
                    for l in left:
                        for r in right:
                            if c == '+':
                                res.append(l + r)
                            elif c == '-':
                                res.append(l - r)
                            elif c == '*':
                                res.append(l * r)
            # 如果res为空，说明表达式是一个数字
            if not res:
                res.append(int(expression[start:end + 1]))

            # 将结果存入缓存
            memo[(start, end)] = res
            return res

        # 调用递归函数
        return ways(expression, 0, len(expression) - 1)

# 示例调用
sol = Solution()
print(sol.diffWaysToCompute("2-1-1"))  # 输出: [0, 2]
print(sol.diffWaysToCompute("2*3-4*5"))  # 输出: [-34, -14, -10, -10, 10]
