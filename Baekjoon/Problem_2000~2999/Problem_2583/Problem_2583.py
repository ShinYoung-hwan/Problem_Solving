import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
inBoard = lambda r, c: (0 <= r < M) and (0 <= c < N)

dr = [ -1, 1, 0, 0 ]
dc = [ 0, 0, -1, 1 ]

def bfs(r0, c0):
    global visited
    cnt = 1
    queue = deque([ (r0, c0) ])
    visited[r0][c0] = True
    
    while queue:
        r0, c0 = queue.popleft()
        
        for i in range(4):
            r, c = r0 + dr[i], c0 + dc[i]
            
            if not inBoard(r, c): continue
            elif board[r][c] == 1: continue
            elif visited[r][c]: continue
            
            queue.append((r, c))
            visited[r][c] = True
            cnt += 1
    
    return cnt
    
if __name__ == "__main__":
    M, N, K = map(int, input().split())
    
    # 보드판에 직사각형 채우기 O(1,000,000)
    board = [ [ 0 ] * N for _ in range(M) ]
    for _ in range(K):
        ldx, ldy, rux, ruy = map(int, input().split())
    
        for r in range(ldy, ruy):
            for c in range(ldx, rux):
                board[r][c] = 1
    
    # BFS로 각 빈 영역의 너비 구하기 O(10,000)
    visited = [ [ False ] * N for _ in range(M) ]
    cnts = []
    for r in range(M):
        for c in range(N):
            if board[r][c] == 1: continue
            elif visited[r][c]: continue
            
            cnts.append(bfs(r, c))
            
    cnts.sort()
    print(len(cnts))
    print(*cnts)
    