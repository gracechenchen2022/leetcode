class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Runtime 557 ms Beats 45.21%
        # heapify(nums)
        # while len(nums) > k:
        #     heappop(nums)
        # return nums[0]

        # Runtime 483 ms Beats 92.71%
        # heap = []
        # it_nums = iter(nums)
        # for _ in range(k):
        #     heappush(heap, next(it_nums))
        # for val in it_nums:
        #     if val > heap[0]:
        #         heappushpop(heap, val)
        # return heap[0]
        
        # Runtime 482 ms Beats 93.32%
        heap = nums[:k]
        heapify(heap)
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heappushpop(heap, nums[i])
        return heap[0]