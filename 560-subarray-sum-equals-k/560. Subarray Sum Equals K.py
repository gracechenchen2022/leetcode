class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0:1} # 0:1, 1:1, 2:1, 3:1
        current_sum = 0
        count = 0
        for num in nums:
            current_sum += num # 1,2,3
            if current_sum - k in prefix_sum:
                count += prefix_sum[current_sum-k] #0+1 = 1, 2
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
        return count