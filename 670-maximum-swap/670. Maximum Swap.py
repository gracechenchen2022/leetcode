class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = list(str(num))
        n = len(num_list)
        right_max = [0]*n
        max_index = n - 1
        right_max[-1] = max_index
        for i in range(n-2, -1, -1):
            if num_list[i] > num_list[max_index]:
                max_index = i
            right_max[i] = max_index
        for i in range(n):
            if num_list[right_max[i]]>num_list[i]:
                num_list[i], num_list[right_max[i]] = num_list[right_max[i]], num_list[i]
                break
        return int(''.join(num_list))