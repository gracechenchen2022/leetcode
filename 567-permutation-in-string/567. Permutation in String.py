class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False
#先计算 s1 中每个字符的频率
        s1_count = Counter(s1)
#在 s2 中维护一个与 s1 的长度相同的滑动窗口，并计算这个窗口内每个字符的频率
        window_count = Counter(s2[:len_s1])

        if s1_count == window_count:
            return True
        for i in range(len_s1, len_s2):
            window_count[s2[i]] += 1
            window_count[s2[i - len_s1]] -= 1

            if window_count[s2[i - len_s1]] == 0:
                del window_count[s2[i - len_s1]]
 #每次移动滑动窗口，我们检查窗口内的字符频率是否与 s1 的字符频率相同。如果相同，则 s2 包含 s1 的一个排列。           
            if s1_count == window_count:
                return True

        return False

'''
时间复杂度: O(n)，其中 n 是字符串 s2 的长度。因为我们在每次滑动窗口时，只进行常数时间的字符计数更新和比较。
空间复杂度: O(1)，因为我们只需要常数空间来存储字符频率计数（字母表大小固定为26个小写字母）。

'''