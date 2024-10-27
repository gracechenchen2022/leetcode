class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(len(s)):
            distance_to_a = (ord(s[i]) - ord('a'))
            distance_to_a_backward = (ord('z') - ord(s[i])+1)
            min_dis = min(distance_to_a, distance_to_a_backward)
            if min_dis <= k:
                k -= min_dis
                s[i] = 'a'
            else:
                s[i] = chr(ord(s[i])-k)
                k = 0
                break
        return ''.join(s)
        