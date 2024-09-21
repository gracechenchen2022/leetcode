from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 将所有数字转换成字符串
        nums = list(map(str, nums))
        
        # 自定义排序规则，比较组合的大小
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        # 使用 sorted 函数进行排序，并传入自定义的比较函数
        nums.sort(key=cmp_to_key(compare))
        
        # 排序后将数字拼接成字符串
        result = ''.join(nums)
        
        # 如果拼接后的结果是以 "0" 开头，说明全是 0，返回 "0"
        return '0' if result[0] == '0' else result
