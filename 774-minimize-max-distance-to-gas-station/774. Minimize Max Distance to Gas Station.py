class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        left = 0.0
        right = 10**8
        E = 0.1**6

        while left < right - E:
            mid = (left + right)/2
            cnt = 0
            for i in range(1, len(stations)):
                cnt += int((stations[i] - stations[i-1])/mid)
            if cnt <= k:
                right = mid
            else:
                left = mid
        return left
                     