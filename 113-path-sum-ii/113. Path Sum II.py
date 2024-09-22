# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, current_path, current_sum):
            if not node:
                return
            current_path.append(node.val)
            current_sum += node.val
            if not node.left and not node.right and current_sum  == targetSum:
                res.append(list(current_path))
            dfs(node.left, current_path, current_sum)
            dfs(node.right, current_path, current_sum)
            current_path.pop()
            
        dfs(root,[], 0)
        return res