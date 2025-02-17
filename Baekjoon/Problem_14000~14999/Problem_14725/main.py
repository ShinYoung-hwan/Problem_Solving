import sys

input = lambda: sys.stdin.readline().rstrip()

class TrieNode:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    def __init__(self):
        self.head = TrieNode(None)
        
    def insert(self, v):
        cur = self.head
        
        for e in v:
            if e not in cur.children:
                cur.children[e] = TrieNode(v)
                
            cur = cur.children[e]
            
        cur.data = v
        
    def dfs(self, cur=None, depth=0):
        if cur is None:
            cur = self.head
        
        if cur.data is not None:
            return
        
        for k in sorted(cur.children.keys()):
            print("-" * (2 * depth) + k)
            self.dfs(cur.children[k], depth+1)    

if __name__ == "__main__":
    N = int(input())
    
    trie = Trie()
    for _ in range(N):
        line = input().split()
        K = int(line[0])
        infos = line[1:]
        
        trie.insert(infos)
        
    trie.dfs()
    