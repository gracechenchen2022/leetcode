class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
       
    # 将字典转为集合以加速查找
        word_set = set(wordDict)
        # 用于记忆化的字典
        memo = {}

        # 判断从某个位置开始的字符串的所有分割方案
        def backtrack(start):
            # 如果已经计算过，直接返回结果
            if start in memo:
                return memo[start]
            # 如果到达字符串末尾，返回空列表
            if start == len(s):
                return [""]

            # 保存当前部分的所有可能结果
            res = []
            # 遍历字符串，从 start 开始
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if substring in word_set:
                    # 找到分割后剩余部分的所有方案
                    sublist = backtrack(end)
                    for sub in sublist:
                        if sub:
                            res.append(substring + " " + sub)
                        else:
                            res.append(substring)
            
            # 记忆化结果
            memo[start] = res
            return res

        # 判断字符串是否可以拆分
        def canBreak(s, wordDict):
            dp = [False] * (len(s) + 1)
            dp[0] = True
            for i in range(1, len(s) + 1):
                for j in range(i):
                    if dp[j] and s[j:i] in word_set:
                        dp[i] = True
                        break
            return dp[-1]

        # 如果无法拆分，直接返回空列表
        if not canBreak(s, wordDict):
            return []

        # 通过回溯得到所有结果
        return backtrack(0)
    