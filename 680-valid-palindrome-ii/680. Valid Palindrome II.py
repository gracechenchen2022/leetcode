class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s: str, left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1

        if left >= right:
            return True

        # Try to skip one character either from left or right
        return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)

# Example usage:
solution = Solution()
print(solution.validPalindrome("abca"))  # Output: True
print(solution.validPalindrome("aba"))   # Output: True
print(solution.validPalindrome("abc"))   # Output: False
