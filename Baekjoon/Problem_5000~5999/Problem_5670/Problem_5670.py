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
        
    def insert(self, s: str):
        """ s를 trie에 삽입한다.  """
        cur = self.head
        
        for c in s:
            if c not in cur.children:
                cur.children[c] = TrieNode(c)
                
            cur = cur.children[c]
        cur.data = s
    
    def search(self, s: str) -> int:
        """ 주어진 문자를 찾기 위해 총 몇번 단어를 입력해야하는지 확인 """
        cnt = 0
        
        cur = self.head
        idx = 0
        
        # 글자를 찾을때까지 반복한다.
        while s != cur.data:
            cnt += 1
            cur = cur.children[s[idx]]
            idx += 1    
            
            # 자식이 하나밖에 없으면 계속 내려간다.    
            while idx < len(s) and cur.data is None and len(cur.children) == 1:
                cur = cur.children[s[idx]]
                idx += 1
                
                if s == cur.data: break
        
        return cnt
        
if __name__ == "__main__":
    while True:
        try:
            N = int(input()) # 사전에 속한 단어의 개수
            trie = Trie()
            
            S = [ input() for _ in range(N) ]
            
            # 사전 정리
            for s in S:
                trie.insert(s)
            
            # 평균 횟수 구하기
            answer = 0.0
            for s in S:
                answer += trie.search(s)
                
            print(f"{answer / N:.2f}")

        except:
            break
        