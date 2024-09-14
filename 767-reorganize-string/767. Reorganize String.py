import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        from collections import Counter


        # 统计每个字符的频率
        freq = Counter(s)
        
        # 找到字符最多能出现的次数，不能超过 (len(s) + 1) // 2
        max_freq = (len(s) + 1) // 2
        # 如果某个字符出现的次数超过一半，直接返回空字符串
        if any(count > max_freq for count in freq.values()):
            return ""
        
        # 使用最大堆（Python的heapq是最小堆，所以我们存储负数以实现最大堆）
        max_heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(max_heap)
        
        # 用来存放重排后的结果
        result = []
        
        # 进行字符重新排列
        prev_count, prev_char = 0, ''
        
        while max_heap:
            # 取出堆顶的字符和对应的频率
            count, char = heapq.heappop(max_heap)
            # 将当前字符加入结果
            result.append(char)
            
            # 如果前一个字符还可以继续使用，重新加入堆中
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))
            
            # 更新当前字符的剩余次数，准备下一轮的比较
            prev_count, prev_char = count + 1, char  # count + 1 因为我们存储的是负数，表示消耗一个字符
        
        # 最后将结果数组合并成字符串并返回
        return ''.join(result)
