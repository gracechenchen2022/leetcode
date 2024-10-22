class Solution {
    public int reverse(int x) {
    int reversed = 0;  // 存储反转后的结果
    while (x != 0) {
        int pop = x % 10;  // 取出x的最后一位数字
        x /= 10;  // 移除x的最后一位数字
        // 检查反转后的结果是否会溢出
        if (reversed > Integer.MAX_VALUE / 10 || (reversed == Integer.MAX_VALUE / 10 && pop > 7)) {
            return 0;
        }
        if (reversed < Integer.MIN_VALUE / 10 || (reversed == Integer.MIN_VALUE / 10 && pop < -8)) {
            return 0;
        }
        reversed = reversed * 10 + pop;  // 将数字添加到反转结果中
    }
    return reversed;
}

}