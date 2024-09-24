class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        res = []
        path = []
        backtrack (0, path)
        return res


    #tc:o(n*2^n)
    #总子集数量 2^n 这是因为每个元素有两种选择要么出现在子集中 要么不出现
    #构建每个子集的时间 复制path到res 需要o(n)
    #sc:o(n) 递归栈决定n次的空间 路径变量 最大长度n