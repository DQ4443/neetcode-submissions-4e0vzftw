class MinStack:
    # use stack to keep track of lowest point in time

    def __init__(self):
        self.stack = []
        self.mins = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if self.mins:
            self.mins.append(min(self.mins[-1], val))
        else:
            self.mins.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.mins:
            return self.mins[-1]
