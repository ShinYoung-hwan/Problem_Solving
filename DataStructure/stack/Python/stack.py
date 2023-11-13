class Stack():
    def __init__(self, lst=None):
        if lst == None:
            self.items = list()
            self.top = 0
        else:
            self.items = lst
            self.top = len(lst)
        
    def is_empty(self):
        return self.top == 0
    
    def peek(self):
        if self.is_empty():
            return False
        return self.items[-1]
    
    def push(self, item):
        self.top += 1
        return self.items.append(item)
    
    def pop(self):
        if self.is_empty(): 
            return False
        
        self.top -= 1
        return self.items.pop()
