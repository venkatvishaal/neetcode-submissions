class MinStack:

    def __init__(self):
        self.stack=[] # empty stack to push and pop
        self.mins=[] # empty stack to find the min elemnt
        

    def push(self, val: int) -> None:
        self.stack.append(val) # push 
        val=min(val,self.mins[-1] if self.mins else val) # find the min value 
        self.mins.append(val) # append min value in that stack
        

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.mins[-1]
        
