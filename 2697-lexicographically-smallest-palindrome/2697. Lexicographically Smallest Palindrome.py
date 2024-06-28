class Solution:
  def makeSmallestPalindrome(self, s: str) -> str:
    s, l = list(s), len(s)
    for i in range(l // 2):
      if s[i] != s[l - i - 1]:
        c = min(s[i], s[l - i - 1])
        s[i], s[l - i - 1] = c, c
    
    return ''.join(s)