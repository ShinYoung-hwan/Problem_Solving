import sys

input = lambda: sys.stdin.readline().rstrip()

class TrieNode(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    def __init__(self):
        self.head = TrieNode(None)
        
    def insert(self, s: str):
        """ 원소 삽입
            시간복잡도 O(N)
        """
        cur = self.head
        
        for c in s:
            if c not in cur.children:
                cur.children[c] = TrieNode(c)
            cur = cur.children[c]
        cur.data = s
    
    def find_prefix(self, s: str):
        """ 원소 확인
            시간복잡도 O(N)
        """
        cur = self.head
        for c in s:
            if c not in cur.children: return False
            cur = cur.children[c]
        
        return True

if __name__ == "__main__":
    N, M = map(int, input().split())
    
    # N개의 S에 해당하는 문자열
    trie = Trie()
    for _ in range(N):
        s = input()
        trie.insert(s)
    
    # M개의 검사대상 문자열
    answer = 0
    for _ in range(M):
        s = input()
        if trie.find_prefix(s): answer += 1
    print(answer)