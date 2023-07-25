class Stack:
    """class for stack data type"""
    def __init__(self, limit= 10):
        self.stack = []
        self.limit = limit
        
    def push(self, data):
        """inserting data to stack"""
        if len(self.stack) >= self.limit:
            print("Stack overflow")
            return 
        self.stack.append(data)
    
    def pop(self):
        """popping or removing data from stack"""
        if len(self.stack) <= 0:
            print("Stack under flow")
            return
        return self.stack.pop()
    
    def top(self):
        """peeking top element of the stack"""
        if len(self.stack) <= 0:
            print("Stack is under flow")
            return
        return self.stack[-1]
    
    def size(self):
        """counting element stored on stack"""
        return len(self.stack)
    
    def display(self):
        """Displaying element of stack"""
        for item in self.stack:
            print(item)

        