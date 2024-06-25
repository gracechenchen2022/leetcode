from bisect import bisect_left
from math import log

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k == 0:
            return 0
        prefix = [log(1)]
        ans = 0
        for num in nums:
            prefix.append(prefix[-1] + log(num))
        for i, val in enumerate(prefix):
            target = log(k) + val
            idx = bisect_left(prefix, target)
            ans += max(0, idx - i - 1)
        return ans 