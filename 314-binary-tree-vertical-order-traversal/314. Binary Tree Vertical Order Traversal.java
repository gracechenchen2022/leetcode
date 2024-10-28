/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
import java.util.*;

class Solution {
    public List<List<Integer>> verticalOrder(TreeNode root) {
        List<List<Integer>> results = new ArrayList<>();
        if (root == null) return results;

        // 使用 TreeMap 保持列的顺序
        Map<Integer, List<Integer>> columnTable = new TreeMap<>();
        Queue<Pair<TreeNode, Integer>> queue = new LinkedList<>();
        queue.offer(new Pair<>(root, 0));  // 根节点列距离为 0

        while (!queue.isEmpty()) {
            Pair<TreeNode, Integer> pair = queue.poll();
            TreeNode node = pair.getKey();
            int column = pair.getValue();

            // 将当前节点值加入到对应列中
            columnTable.computeIfAbsent(column, k -> new ArrayList<>()).add(node.val);

            // 左子树的列距离 -1，右子树的列距离 +1
            if (node.left != null) {
                queue.offer(new Pair<>(node.left, column - 1));
            }
            if (node.right != null) {
                queue.offer(new Pair<>(node.right, column + 1));
            }
        }

        // 将结果按列顺序添加到结果列表
        for (List<Integer> col : columnTable.values()) {
            results.add(col);
        }

        return results;
    }

    // Pair class to hold TreeNode and its column index
    private static class Pair<K, V> {
        private K key;
        private V value;
        public Pair(K key, V value) {
            this.key = key;
            this.value = value;
        }
        public K getKey() { return key; }
        public V getValue() { return value; }
    }
}
