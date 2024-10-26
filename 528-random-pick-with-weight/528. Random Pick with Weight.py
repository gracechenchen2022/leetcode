class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        current_sum = 0
        for weight in w:
            current_sum += weight
            self.prefix_sum.append(current_sum)
        self.total_weight = current_sum

    def pickIndex(self) -> int:
        target = random.randint(1, self.total_weight)
        left, right = 0, len(self.prefix_sum)-1
        while left < right:
            mid = (left+right)//2
            if self.prefix_sum[mid] < target:
                left = mid+1
            else:
                right = mid
        return left
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()