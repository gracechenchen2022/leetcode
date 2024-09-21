# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_map= {}
        def dfs(node, parent):
            if node:
                parent_map[node] = parent
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root, None)
        queue = [(target, 0)]
        seen = {target}
        result = []
        while queue:
            node, dist = queue.pop(0)
            if dist == k:
                result.append(node.val)
            elif dist < k:
                for neighbor in (node.left, node.right, parent_map[node]):
                    if neighbor and neighbor not in seen:
                        seen.add(neighbor)
                        queue.append((neighbor,dist+1))
        return result