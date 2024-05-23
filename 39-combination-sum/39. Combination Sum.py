class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        current_combination = []
        def backtrack(start, current_sum):
            if current_sum == target:
                res.append(current_combination[:])
                return 
            if current_sum > target:
                return 
            for i in range(start, len(candidates)):
                current_combination.append(candidates[i])
                backtrack(i, current_sum + candidates[i])
                current_combination.pop()
        backtrack(0,0)
        return res
                
