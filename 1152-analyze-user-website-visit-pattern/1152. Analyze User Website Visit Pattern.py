class Solution:
    
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # 使用 defaultdict 来存储每个用户访问的网站序列
        users = defaultdict(list)
        # 将 username, timestamp 和 website 组合在一起，并按用户名和时间排序
        for user, time, site in sorted(zip(username, timestamp, website), key=lambda x: (x[0], x[1])):
            users[user].append(site)  # 将每个用户按时间顺序访问的网站加入其访问列表中
        # 创建 Counter 来记录每种三网站组合的出现次数
        patterns = Counter()
        # 遍历每个用户及其访问的网站序列
        for user, sites in users.items():
            # 更新 Counter，计算每个用户访问过的所有三网站组合（使用 set 去重）
            patterns.update(Counter(set(combinations(sites, 3))))
        # 返回出现次数最多的三网站组合，如果有多个，按字母顺序返回最小的
        return max(sorted(patterns), key=patterns.get)



