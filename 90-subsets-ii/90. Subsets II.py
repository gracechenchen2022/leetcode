class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        
        nums.sort()
        res=[]
        path =[]
        backtrack(0,[])
        return res


# 时间复杂度
# 对于每个元素，我们有两种选择：包括它或不包括它。
# 在没有重复元素的情况下，总共有 2^n 个子集，其中 n 是数组的长度。
# 由于存在重复元素，我们需要通过排序和跳过重复元素来避免生成重复子集。
# 因此，时间复杂度为 O(n log n + 2^n)。

# 空间复杂度
# 空间复杂度主要由递归调用堆栈的深度和存储结果的空间决定。
# 1. 递归调用堆栈：最坏情况下，递归调用堆栈的深度为 O(n)。
# 2. 存储结果：我们需要存储所有子集，子集的总数最多为 2^n，
#    每个子集的长度最多为 n，因此存储结果的空间复杂度为 O(n * 2^n)。
# 因此，总的空间复杂度为 O(n + n * 2^n)。

# 总结
# 时间复杂度: O(n log n + 2^n)
# 空间复杂度: O(n + n * 2^n)
