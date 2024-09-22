class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = n*(1+n)//2
        sum_nums = sum(nums)
        return total_sum - sum_nums