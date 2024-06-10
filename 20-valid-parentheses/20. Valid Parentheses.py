class Solution:
    def isValid(self, s: str) -> bool:
        # 字典用于存储每种右括号对应的左括号
        bracket_map = {')': '(', '}': '{', ']': '['}
        # 栈用于存储遇到的左括号
        stack = []

        # 遍历字符串中的每个字符
        for char in s:
            if char in bracket_map:
                # 如果当前字符是右括号，从栈中弹出一个元素，如果栈为空则使用一个哑值
                top_element = stack.pop() if stack else '#'
                # 如果当前右括号的对应左括号与栈顶元素不匹配，返回 False
                if bracket_map[char] != top_element:
                    return False
            else:
                # 如果当前字符是左括号，压入栈中
                stack.append(char)

        # 如果栈为空，说明所有的左括号都被正确匹配
        return not stack

