class Deq():
    def __init__(self):
        self.items = list()
        self.size = 0
        
    def is_empty(self):
        return self.size == 0
    
    def add_front(self, item):
        self.size += 1
        self.items.insert(0, item)
        
    def add_read(self, item):
        self.size += 1
        self.items.append(item)
        
    def remove_front(self):
        if self.is_empty():
            return False
        self.size -= 1
        return self.items.pop(0)
    
    def remove_rear(self):
        if self.is_empty():
            return False
        self.size -= 1
        return self.items.pop()
    
    def peek_front(self):
        if self.is_empty():
            return False
        return self.items[0]
    
    def peek_rear(self):
        if self.is_empty():
            return False
        return self.items[-1]