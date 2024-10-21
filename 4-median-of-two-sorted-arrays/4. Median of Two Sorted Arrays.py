class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 确保nums1是较短的数组
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2

        # 在nums1中进行二分查找
        low, high = 0, m
        while low < high:
            i = low + (high - low) // 2
            j = total_left - i
            if nums1[i] < nums2[j - 1]:
                # i 需要增大
                low = i + 1
            else:
                # i 已经足够大或需要减小
                high = i
        i = low
        j = total_left - i
        nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
        nums1_right_min = float('inf') if i == m else nums1[i]
        nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
        nums2_right_min = float('inf') if j == n else nums2[j]

        if (m + n) % 2 == 1:
            return max(nums1_left_max, nums2_left_max)
        else:
            return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2
