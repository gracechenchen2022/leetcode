class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        if not nums or k == 0:
            return []
        n = len(nums)
        if k == 1:
            return nums
        deque_index = deque()
        max_values = []
        for i in range(n):
            # 移除不在当前窗口的元素
            if deque_index and deque_index[0] < i - k + 1:
                deque_index.popleft()
            
            # 移除所有小于当前元素的元素
            while deque_index and nums[deque_index[-1]] < nums[i]:
                deque_index.pop()
            
            # 添加当前元素的索引
            deque_index.append(i)
            
            # 从第k个元素开始，每次加入最大值到结果中
            if i >= k - 1:
                max_values.append(nums[deque_index[0]])
        
        return max_values
'''
时间复杂度：O(n)，每个元素最多被添加和移除一次。
空间复杂度：O(k)，双端队列最多存储 k 个元素的索引。

'''