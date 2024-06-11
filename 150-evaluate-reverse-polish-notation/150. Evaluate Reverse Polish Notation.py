class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
       
        stack = []
        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                elif token == '/':
                    # Python除法默认是浮点除法，题目要求整数除法，且向零取整
                    result = int(a / b)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[0]
