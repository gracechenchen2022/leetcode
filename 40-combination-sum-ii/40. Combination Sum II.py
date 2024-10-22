class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, current_sum, current_combination):
            if current_sum == target:
                res.append(list(current_combination))
                return
            if current_sum > target:
                return
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                current_combination.append(candidates[i])
                backtrack(i + 1, current_sum + candidates[i], current_combination)
                current_combination.pop()
        candidates.sort()
        res = []
        backtrack(0,0,[])
        return res
# 时间复杂度
# 在最坏的情况下，组合总和问题的复杂度取决于生成所有可能的组合。
# 1. 排序时间: 首先，我们需要对输入数组进行排序，时间复杂度为 O(n log n)。
# 2. 生成组合: 对于每个元素，我们有选择包括它或不包括它的选项。
#    子集的总数最多为 2^n，但实际情况会因为剪枝而有所减少。
#    生成每个组合的过程是递归的，最坏情况下时间复杂度接近 O(2^n)。
# 综合考虑，时间复杂度为 O(n log n + 2^n)。

# 空间复杂度
# 空间复杂度主要由递归调用堆栈的深度和存储结果的空间决定。
# 1. 递归调用堆栈: 最坏情况下，递归调用堆栈的深度为 O(n)。
# 2. 存储结果: 我们需要存储所有满足条件的组合，
#    组合的总数最多为 2^n，每个组合的长度最多为 n。
#    因此，存储结果的空间复杂度为 O(n * 2^n)。
# 因此，总的空间复杂度为 O(n + n * 2^n)。

# 总结
# 时间复杂度: O(n log n + 2^n)
# 空间复杂度: O(n + n * 2^n)
