class Solution {
    public int[][] merge(int[][] intervals) {
        List<int[]>res = new ArrayList<>();
        if(intervals == null || intervals.length == 0) return new int[0][];
        Arrays.sort(intervals,(a,b)->a[0]-b[0]);
        int[]cur = intervals[0];
        for(int[]next:intervals){
            if(cur[1]>=next[0])cur[1] = Math.max(cur[1], next[1]);
            else{
                res.add(cur);
                cur = next;
            }
        }
        res.add(cur);
        return res.toArray(new int[0][]);
    }
}