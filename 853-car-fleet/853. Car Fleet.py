class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        fleets = 0 #车队数量
        time = 0
        for p, s in cars:
            t = (target-p)/s
            if t > time:
                fleets += 1
                time = t
        return fleets

            
