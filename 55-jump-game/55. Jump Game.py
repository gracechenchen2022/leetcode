class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 当前能够到达的最远位置
        max_reachable = 0
        
        # 遍历数组中的每个位置
        for i in range(len(nums)):
            # 如果当前位置超过了当前能够到达的最远位置，直接返回False
            if i > max_reachable:
                return False
            
            # 更新能够到达的最远位置
            max_reachable = max(max_reachable, i + nums[i])
            
            # 如果能够到达或超过最后一个位置，直接返回True
            if max_reachable >= len(nums) - 1:
                return True
        
        return False
