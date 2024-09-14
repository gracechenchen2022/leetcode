class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {'(': ')', '[': ']', '{': '}'}
        stack = [] 
        for char in s:
            if char in bracket_map:
                stack.append(bracket_map[char])
            else:
                if not stack or stack.pop() != char:
                    return False
        
        return not stack
