import java.util.LinkedList;
import java.util.Queue;

public class Solution {
    public int[][] updateMatrix(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] dist = new int[m][n];
        Queue<int[]> queue = new LinkedList<>();
        
        // Initialize the dist matrix and the queue.
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    dist[i][j] = 0;
                    queue.add(new int[]{i, j});
                } else {
                    dist[i][j] = Integer.MAX_VALUE;
                }
            }
        }
        
        // Directions array.
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        
        // BFS
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            for (int[] dir : dirs) {
                int row = curr[0] + dir[0];
                int col = curr[1] + dir[1];
                if (row < 0 || col < 0 || row >= m || col >= n || dist[row][col] <= dist[curr[0]][curr[1]] + 1) {
                    continue;
                }
                queue.add(new int[]{row, col});
                dist[row][col] = dist[curr[0]][curr[1]] + 1;
            }
        }
        
        return dist;
    }
}
