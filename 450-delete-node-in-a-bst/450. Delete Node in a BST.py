# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None  # 如果树为空，直接返回 None
        
        # 1. 查找要删除的节点
        if key < root.val:
            # 如果 key 小于当前节点值，递归处理左子树
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            # 如果 key 大于当前节点值，递归处理右子树
            root.right = self.deleteNode(root.right, key)
        else:
            # 找到了要删除的节点
            
            # 2. 处理没有子节点或者只有一个子节点的情况
            if not root.left:  # 如果左子节点为空，返回右子树
                return root.right
            elif not root.right:  # 如果右子节点为空，返回左子树
                return root.left
            
            # 3. 处理有两个子节点的情况，找到右子树中的最小节点（后继节点）
            min_larger_node = self.findMin(root.right)
            root.val = min_larger_node.val  # 用后继节点的值替换当前节点的值
            # 删除后继节点
            root.right = self.deleteNode(root.right, min_larger_node.val)
        
        return root
    
    # 辅助函数，寻找右子树的最小节点（后继）
    def findMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left  # 一直向左找到最小节点
        return node
