# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        # 定义函数f，计算每个节点到其最深子节点的距离
        def f(root):
            if root is None:  # 如果节点为空，则返回深度为0
                return 0
            l, r = f(root.left), f(root.right)  # 递归计算左右子树的深度
            d[root] = 1 + max(l, r)  # 当前节点的深度是其子节点深度的最大值加一
            return d[root]

        # 定义函数dfs，递归遍历树，计算每个节点的res值
        def dfs(root, depth, rest):
            if root is None:  # 如果节点为空，直接返回
                return
            depth += 1  # 当前深度加一
            res[root.val] = rest  # 存储当前节点的res值
            # 检查并递归左子树，计算rest时考虑右子树的深度
            left_depth = d[root.left] if root.left else 0
            right_depth = d[root.right] if root.right else 0
            dfs(root.left, depth, max(rest, depth + right_depth))
            # 检查并递归右子树，计算rest时考虑左子树的深度
            dfs(root.right, depth, max(rest, depth + left_depth))

        d = defaultdict(int)  # 创建一个字典，用于存储每个节点的最大深度
        f(root)  # 计算每个节点的最大深度
        # 初始化res数组，长度为树中节点值的最大值加一
        res = [0] * (max(d.keys(), key=lambda x: x.val).val + 1)
        dfs(root, -1, 0)  # 从根节点开始递归遍历树
        # 返回查询结果，queries中每个节点对应的res值
        return [res[v] for v in queries if v < len(res)]