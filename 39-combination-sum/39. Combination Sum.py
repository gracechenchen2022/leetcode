class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, current_sum, current_combination):
            if current_sum == target:
                res.append(list(current_combination))
                return 
            if current_sum > target:
                return 
            for i in range(start, len(candidates)):            
                current_combination.append(candidates[i])
                backtrack(i, current_sum+candidates[i],current_combination)
                current_combination.pop()
        res = []
        backtrack(0,0,[])
        return res

