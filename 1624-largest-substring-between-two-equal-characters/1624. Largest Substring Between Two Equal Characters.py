class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_index = {}
        max_len = -1
        
        for i, char in enumerate(s):
            if char in char_index:
                max_len = max(max_len, i - char_index[char] - 1)
            else:
                char_index[char] = i
        
        return max_len