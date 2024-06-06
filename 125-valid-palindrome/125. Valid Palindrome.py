class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

          
"""
   这个回文字符串判断的算法的时间复杂度是 O(n)，其中 n 是输入字符串 s 的长度。这是因为在算法中，我们只对字符串 s 进行一次线性扫描，同时使用两个指针 l 和 r，这两个指针最多各自移动 n/2 次。

空间复杂度是 O(1)，因为除了输入字符串 s 外，算法只使用了常数额外的空间，即 l 和 r 两个指针和一些常数大小的辅助变量。

因此，该算法是具有很好时间复杂度和空间复杂度的有效解决方案。
"""