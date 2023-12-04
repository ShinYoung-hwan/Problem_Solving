from collections import deque

class BTree:...
class Node:...

class Node:
    def __init__(self, item=None):
        self.item = item
        self.left_child = None
        self.right_child = None
        
    def set_item(self, item):
        self.item = item
    
    def set_left_subtree(self, left_subtree: BTree):
        self.left_child = left_subtree
        
    def set_right_sub_tree(self, right_subtree):
        self.right_child = right_subtree
        
    def __repr__(self) -> str:
        return f'<Node: {str(self.item)}>'

class BTree:
    def __init__(self):
        self.root: Node|None = None
    
    def set_root(self, node):
        self.root = node
    
    def traversal_inorder(self):
        # LCR
        print('Inorder:', end=' ')
        def _inorder(root: Node):
            if(root.left_child is not None):
                _inorder(root.left_child)
            print(root.item, end=' ')
            if(root.right_child is not None):
                _inorder(root.right_child)
        _inorder(self.root)
        print()
    
    def traversal_preorder(self):
        # CLR
        print('Preorder:', end=' ')
        def _preorder(root: Node):
            print(root.item, end=' ')
            if(root.left_child is not None):
                _preorder(root.left_child)
            if(root.right_child is not None):
                _preorder(root.right_child)
        _preorder(self.root)
        print()
        
    def traversal_postorder(self):
        # LRC
        print('Postorder:', end=' ')
        def _postorder(root: Node):
            if(root.left_child is not None):
                _postorder(root.left_child)
            if(root.right_child is not None):
                _postorder(root.right_child)
            print(root.item, end=' ')
        _postorder(self.root)
        print()
        
    def traversal_levelorder(self):
        # each level, left to right
        print('Levelorder:', end=' ')
        queue = deque()
        queue.append(self.root)
        
        while len(queue) != 0:
            cur_node:Node = queue.popleft()
            print(cur_node.item, end=' ')
            if cur_node.left_child is not None:
                queue.append(cur_node.left_child)
            if cur_node.right_child is not None:
                queue.append(cur_node.right_child)
        print('')
        
    def get_nNodes(self):
        def _nNodes(node: Node):
            r, l = 0, 0
            if node.right_child is not None:
                r = _nNodes(node.right_child)
            if node.left_child is not None:
                l = _nNodes(node.left_child)
            return 1 + r + l
        return _nNodes(self.root)
    
    def get_height(self):
        def _height(node: Node):
            r, l = 0, 0
            if node.right_child is not None:
                r = _height(node.right_child)
            if node.left_child is not None:
                l = _height(node.left_child)
            return 1 + max(r, l)
        return _height(self.root)
        
    
if __name__ == "__main__":
    
    btree = BTree()
    n1 = Node(1)
    n2 = Node(2)
    n2.set_left_subtree(Node(4))
    n2.set_right_sub_tree(Node(5))
    n3 = Node(3)
    n3.set_left_subtree(Node(6))
    n3.set_right_sub_tree(Node(7))
    
    n1.set_left_subtree(n2)
    n1.set_right_sub_tree(n3)
    btree.set_root(n1)
    
    btree.traversal_inorder()
    btree.traversal_preorder()
    btree.traversal_postorder()
    btree.traversal_levelorder()
    print(btree.get_nNodes())
    print(btree.get_height())