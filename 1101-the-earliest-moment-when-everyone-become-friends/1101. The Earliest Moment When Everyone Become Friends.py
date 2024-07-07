class DSU:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.rank = [1] * N
        self.components = N
        
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        ua = self.find(a)
        ub = self.find(b)
        if ua == ub:
            return False
        
        if self.rank[ua] < self.rank[ub]:
            ua, ub = ub, ua
            
        self.parent[ub] = ua
        self.rank[ua] += self.rank[ub]
        self.rank[ub] = self.rank[ua]
        self.components -= 1
        return True
    
    def rank(self, x):
        return self.rank[self.find(x)]

    
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        uf = DSU(n)
        for t, u, v in logs:
            uf.union(u, v)
            if uf.components == 1:
                return t
        return -1
        # Time: O(m * log(m) + n + m * α(n)) 
        #       where m is the length of logs and n the number of people. O(n) is for the initialization of union find
        # Space: O(m + n)
        #        O(m) is for Python's Timsort algorithm, O(n) for the initialization of union find
            