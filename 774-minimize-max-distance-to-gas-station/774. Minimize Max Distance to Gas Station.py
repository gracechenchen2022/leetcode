class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        left = 0.0
        right = 10**8
        E = 1e-6  # 浮点精度

        while right - left > E:
            mid = (left + right) / 2
            cnt = 0
            for i in range(1, len(stations)):
                # 计算在当前mid下需要增加的加油站数量
                cnt += int((stations[i] - stations[i - 1]) / mid)
            
            # 根据计算出的加油站数量更新左右边界
            if cnt <= k:
                right = mid
            else:
                left = mid

        return left
