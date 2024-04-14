class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)

        # unique指针表示非重复元素的下一个放置位置
        unique = 2

        # 遍历数组，从第三个元素开始
        for i in range(2, len(nums)):
            if nums[i] != nums[unique - 2]:
                nums[unique] = nums[i]
                unique += 1

        return unique

