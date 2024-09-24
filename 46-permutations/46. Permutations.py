class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        seen = set()
        def backtrack(start, path):
            if len(path) == len(nums):
                res.append(path[:])
            for i in nums:
                if i in seen:
                    pass
                else:
                    path.append(i)
                    seen.add(i)
                    backtrack(start, path)
                    path.pop()
                    seen.remove(i)
        backtrack(0,[])
        return res