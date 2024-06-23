class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = curr = l  = 0
        mx = max(nums)
        for r in range(len(nums)):
            curr += nums[r] == mx
            while curr >= k:
                curr -= nums[l] == mx
                l += 1
            ans += l
        return ans