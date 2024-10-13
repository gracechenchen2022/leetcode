class Solution {
    public boolean validWordAbbreviation(String word, String abbr) {
        int i = 0, j = 0;
        while(i < word.length() && j < abbr.length()){
            
            //先暴力判断
            if(word.charAt(i) == abbr.charAt(j)){
                i++;
                j++;
                continue;
            }//小于等于0的就不要
            if(abbr.charAt(j) <= '0' || abbr.charAt(j) > '9'){
                return false;
            }
            int start = j;
            //在(0,9]之间的数字 就继续走从第一个数字start开始算
            while(j < abbr.length() && abbr.charAt(j) >= '0' && abbr.charAt(j) <='9'){
                ++j;
            }
            int num = Integer.valueOf(abbr.substring(start,j));
            i += num;
        }
        return i == word.length() && j == abbr.length();
    }
}