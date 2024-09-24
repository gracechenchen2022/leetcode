class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(left, path, start):
            if left ==0:
                res.append(list(path))
                return
            elif left<0:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(left - candidates[i], path, i)
                path.pop()
        backtrack(target,[],0)
        return res
