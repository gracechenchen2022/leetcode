class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}
        def ways(expression):
            if expression in memo:
                return memo[expression]
            res = []
            for i, c in enumerate(expression):
                if c in "+-*":
                    left = ways(expression[:i])
                    right = ways(expression[i+1:])
                    for l in left:
                        for r in right:
                            if c == '+':
                                res.append(l+r)
                            elif c == '-':
                                res.append(l-r)
                            elif c == '*':
                                res.append(l*r)
            if not res:
                res.append(int(expression))
            memo[expression] = res
            return res
        

        return ways(expression)