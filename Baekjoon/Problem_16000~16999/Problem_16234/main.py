import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
isIn = lambda r, c: (0 <= r < N) and (0 <= c < N)

dr = [ -1, 1, 0, 0 ]
dc = [ 0, 0, -1, 1 ]

def BFS(r0, c0, visited):
    unions = []
    queue = deque()
    queue.append((r0, c0))
    visited[r0][c0] = True
    
    unions.append((r0, c0))
    _sum = A[r0][c0]
    
    while queue:
        r0, c0 = queue.popleft()
        
        for i in range(4):
            r, c = r0 + dr[i], c0 + dc[i]
            
            if not isIn(r, c): continue
            if visited[r][c]: continue
            if not (L <= abs(A[r][c] - A[r0][c0]) <= R): continue
            
            queue.append((r, c))
            visited[r][c] = True
            unions.append((r, c))
            _sum += A[r][c]
    
    return unions, _sum

def move(unions, _sum):
    global A
    print
    n = _sum // len(unions)
    
    for r, c in unions:
        A[r][c] = n    

def move_population():
    visited = [ [ False ] * N for _ in range(N) ]
    
    isMove = False
    for r in range(N):
        for c in range(N):
            if visited[r][c]: continue
            
            unions, _sum = BFS(r, c, visited)
            if len(unions) >= 2:
                isMove = True
                move(unions, _sum)
    
    return isMove

if __name__ == "__main__":
    N, L, R = map(int, input().split())
    A = [ list(map(int, input().split())) for _ in range(N) ]
    
    for day in range(0, 2000):
        # 인구이동 실패
        if not move_population():
            print(day)
            break
        