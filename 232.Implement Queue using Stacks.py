class MyQueue:

    def __init__(self):
        self.queue_list = []

    def push(self, x: int) -> None:
        self.queue_list.append(x)

    def pop(self) -> int:
        if len(self.queue_list) > 0:
            return self.queue_list.pop(0)

    def peek(self) -> int:
        if len(self.queue_list) > 0:
            return self.queue_list[0]

    def empty(self) -> bool:
        if len(self.queue_list) == 0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
obj = MyQueue()