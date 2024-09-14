class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0 
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        total_water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] < left_max:
                    total_water += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if height[right] < right_max:
                    total_water += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1
        return total_water