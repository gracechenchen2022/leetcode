class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:


        max_heap = []
        
        for x, y in points:
            dist = -(x*x + y*y)  # 使用负数来构建最大堆
            if len(max_heap) < K:
                heapq.heappush(max_heap, (dist, x, y))
            else:
                heapq.heappushpop(max_heap, (dist, x, y))
        
        return [[x, y] for (dist, x, y) in max_heap]

