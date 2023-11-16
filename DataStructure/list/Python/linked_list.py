class Node():
    def __init__(self, item):
        self.item = item
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head = Node(None)
        self.len = 0
    
    def is_empty(self):
        return self.len == 0
    
    def insert_first(self, item):
        self.insert_middle(0, item)
    def insert_last(self, item):
        self.insert_middle(self.len, item)
    def insert_middle(self, pos, item):
        if pos > self.len:
            raise IndexError
        cur_node = self.head # dummy node, node idx -1
        for _ in range(pos):
            cur_node = cur_node.next
        
        next_node = cur_node.next 
        cur_node.next = Node(item)
        cur_node.next.next = next_node
        self.len += 1
    
    def remove_first(self):
        self.remove_middle(0)
    def remove_last(self):
        self.remove_middle(self.len-1)
    def remove_middle(self, pos):
        if self.is_empty():
            raise IndexError
        if pos > self.len:
            raise IndexError
        
        cur_node = self.head # dummy node, node idx -1
        for _ in range(pos):
            cur_node = cur_node.next
        prev_node = cur_node
        cur_node = prev_node.next
        next_node = cur_node.next
        prev_node.next = next_node
        del cur_node
        self.len -= 1
        
    def read_item(self, pos):
        cur = self.head.next # node idx 0
        for _ in range(pos):
            cur = cur.next
        print(cur.item)
        
    def print_list(self):
        cur_node = self.head.next # node idx 0
        while cur_node != None:
            print(f'{cur_node.item} -> ', end='')
            cur_node = cur_node.next
        print('None')
        
    def __len__(self):
        return self.len

class CircularLinkedList(LinkedList):
    def __init__(self):
        self.tail

if __name__ == "__main__":
    lList = LinkedList()
    
    lList.insert_first(1)
    lList.insert_last(2)
    lList.insert_last(3)
    lList.remove_middle(1)
    lList.print_list()