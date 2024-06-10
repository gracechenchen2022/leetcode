class MinStack:
    def __init__(self):
        self.stack = []      # 主栈
        self.minStack = []   # 辅助栈，用于存储每一步的最小值

    def push(self, x: int) -> None:
        self.stack.append(x)
        # 辅助栈为空或者当前元素小于等于辅助栈栈顶元素时，压入辅助栈
        if not self.minStack or x <= self.minStack[-1]:
            self.minStack.append(x)

    def pop(self) -> None:
        # 如果弹出的元素等于辅助栈栈顶元素，辅助栈也需要弹出
        if self.stack.pop() == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()