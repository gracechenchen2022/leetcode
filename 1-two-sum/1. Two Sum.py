class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in preMap:
                return(preMap[diff],i)
            preMap[n] = i
# i , n  0, 2; 1, 7; 2, 11; 3, 15;
# target = 9  diff = 9-2 preMap[2] = 0
# diff = 9-7 return  0,1 preMap[]