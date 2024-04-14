class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        p = m + n - 1
         
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:#如果p1 比 p2大
                nums1[p] = nums1[p1] #把p1拷贝过来从大到小
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        nums1[:p2 + 1] = nums2[:p2 + 1] #如果nums2还有剩余元素 直接拷贝到num1的前面