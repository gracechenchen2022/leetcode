class Solution {
    public int minMeetingRooms(int[][] intervals) {
        List<int[]> list = new ArrayList<>();
        for (int[]interval:intervals){
            list.add(new int[]{interval[0],1});
            list.add(new int[]{interval[1],-1});
        }
        Collections.sort(list, new Comparator<int[]>(){
            @Override
            public int compare(int[]a, int[]b){
                return a[0]==b[0]?a[1]-b[1]:a[0]-b[0];
            }
        });
        int res=0,count = 0;
        for(int[]point:list){
            count+=point[1];
            res = Math.max(res,count);
        }
        return res;
    }
    
}