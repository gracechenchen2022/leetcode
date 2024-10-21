class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return[]
        
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def backtrack(index, path):
            if index == len(digits):
                combinations.append("".join(path))
                return 
            possible_letters = phone_map[digits[index]]

            for letter in possible_letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()
        combinations = []
        backtrack(0, [])
        return combinations

# 时间复杂度
# 假设输入字符串的长度为 n。
# 1. 生成所有组合: 每个数字（2-9）对应3到4个字母。
#    对于每个数字，我们需要遍历所有可能的字母组合。
#    在最坏的情况下，每个数字对应4个字母。因此，总的组合数为 4^n。
# 2. 生成每个组合的时间是线性的，即 O(n)。
#    所以，生成所有组合的时间复杂度为 O(n * 4^n)。

# 空间复杂度
# 空间复杂度主要由递归调用堆栈的深度和存储结果的空间决定。
# 1. 递归调用堆栈: 在最坏情况下，递归调用堆栈的深度为输入字符串的长度 n，因此空间复杂度为 O(n)。
# 2. 存储结果: 我们需要存储所有的字母组合，总共有 4^n 个组合，每个组合的长度为 n，
#    因此存储结果的空间复杂度为 O(n * 4^n)。
# 因此，总的空间复杂度为 O(n + n * 4^n)。

# 总结
# 时间复杂度: O(n * 4^n)
# 空间复杂度: O(n + n * 4^n)
