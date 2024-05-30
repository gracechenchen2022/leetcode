class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preMap = {} #o(1)
        for i, n in enumerate(nums): #o(n) iteractions
            diff = target - n #o(1) to get certain elem from array
            if diff in preMap: #o(1) to substract o(1) to check set for number
                return(preMap[diff],i) 
            preMap[n] = i
# i , n  0, 2; 1, 7; 2, 11; 3, 15;
# target = 9  diff = 9-2 preMap[2] = 0
# diff = 9-7 return  0,1 preMap[]
#tc: on, sc: on