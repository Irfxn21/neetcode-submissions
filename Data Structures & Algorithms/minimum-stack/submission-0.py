class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:

        self.stack.append(val)
        

    def pop(self) -> None:

        self.stack.pop()
        

    def top(self) -> int:

        return self.stack[-1]
        

    def getMin(self) -> int:

        for i in range(len(self.stack)):
            if i == 0:
                minimum = self.stack[i]
            else:
                minimum = min(minimum, self.stack[i])
        
        return minimum


        
