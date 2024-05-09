class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        # 输出数组，初始时output[i]设置为1
        output = [1] * n

        # left用来计算当前索引左边所有元素的乘积
        left = 1
        for i in range(n):
            output[i] = left
            left *= nums[i]

        # right用来计算当前索引右边所有元素的乘积
        right = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output
        