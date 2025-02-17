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
        
    def insert(self, s: str) -> bool:
        cur = self.head
        
        for c in s:
            # 이미 접두어로 종료되는 번호가 있는 경우
            if cur.data is not None: return False
            
            if c not in cur.children:
                cur.children[c] = TrieNode(c)
                
            cur = cur.children[c]
            
        cur.data = s
        
        # 더 이어지는 번호가 있지만 먼저 종료되는 경우.
        if cur.children:
            return False
        
        return True

if __name__ == "__main__":
    for _test_case in range(int(input())):
        n = int(input()) # 전화번호 
        trie = Trie()
        answer = "YES"
        
        for _ in range(n):
            s = input()
            
            # 이미 접두어로 있는 경우에는 더이상 삽입 x
            if answer != "YES": continue
            
            if not trie.insert(s):
                answer = "NO"
        
        print(answer)