#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#
import collections
# @lc code=start
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue1.popleft()


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue1[0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue1



# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(2)
obj.push(9)
obj.push(4)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
# @lc code=end

