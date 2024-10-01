class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        max_freq = (len(s) + 1)//2
        if any(count > max_freq for count in freq.values()):
            return ""
        max_heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(max_heap)
        result = []
        prev_count, prev_char = 0, ''
        while max_heap:
            count, char = heapq.heappop(max_heap)
            result.append(char)
            if prev_count < 0:
                heapq.heappush(max_heap,(prev_count,prev_char))
            prev_count, prev_char = count+1, char
        return ''.join(result)