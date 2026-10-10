class MyStackInt:

    def __init__(self):
        self.stack = []
        self.currentMax = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, num: int):
        if self.is_empty():
            self.currentMax.append(num)
        elif num >= self.currentMax[-1]:
            self.currentMax.append(num)
        self.stack.append(num)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        elif self.stack[-1] == self.currentMax[-1]:
            self.currentMax.pop()
        return self.stack.pop()

    def max(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.currentMax[-1]