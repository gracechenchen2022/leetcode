class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        start = 0
        for end in range(len(s)):
            if s[end] == ' ':
                self.reverse_range(s, start, end-1)
                start = end + 1
        self.reverse_range(s, start,len(s)-1)
    def reverse_range(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right],s[left]
            left += 1
            right -= 1