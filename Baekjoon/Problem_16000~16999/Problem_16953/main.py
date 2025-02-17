import sys

from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def bfs(src, dest):
    visited = set()
    visited.add(src)
    queue = deque([ (src, 1) ])
    
    while queue:
        cur, n = queue.popleft()
        if cur == dest: return n
        
        if (next:=2*cur) not in visited and next <= B: # 2배 만들기
            queue.append((next, n+1))
            visited.add(next)
            
        if (next:=int(''.join([str(cur), '1']))) not in visited and next <= B:  # 뒤에 1 붙이기
            queue.append((next, n+1))
            visited.add(next)
        
    return -1

if __name__ == "__main__":
    A, B = map(int, input().split()) # A to B
    
    print(bfs(A, B))
    