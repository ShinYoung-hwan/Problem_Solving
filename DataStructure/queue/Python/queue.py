class Queue():
    def __init__(self, lst=None):
        if lst == None:
            self.items = list()
            self.rear = 0
        else:
            self.items = lst
            self.rear = len(lst)
    
    def is_empty(self):
        return self.rear == 0
    
    def peek(self):
        if self.is_empty():
            return False
        return self.items[0]
    
    def enqueue(self, item):
        self.rear += 1
        self.items.append(item)
        
    def dequeue(self):
        if self.is_empty():
            return False
        self.rear -= 1
        return self.items.pop(0)