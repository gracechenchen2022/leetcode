class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if sum((pile - 1) // mid + 1 for pile in piles) > H:
                left = mid + 1
            else:
                right = mid
        return left