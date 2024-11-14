class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for key, val in count.items():
            heapq.heappush(heap,(val, key))
            if len(heap) > k:
                heapq.heappop(heap)
            top_k = [key for val, key in heap]
        return top_k