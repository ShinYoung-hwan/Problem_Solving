import sys
from collections import deque

PET, WATER = 'S', '*'

input = lambda: sys.stdin.readline().rstrip()
is_in = lambda r, c: (0 <= r < R) and (0 <= c < C)

dr = [ -1, 1, 0, 0 ]
dc = [ 0, 0, -1, 1 ]

q = deque()

def bfs():
    global board
    while q:
        type, cost, r0, c0 = q.popleft()
        
        for i in range(4):
            r, c = r0 + dr[i], c0 + dc[i]

            if not is_in(r, c): continue # 범위를 벗어난 경우
            elif board[r][c] == 'X': continue # 벽을 만난 경우
            elif type == PET and board[r][c] == WATER: continue # 고슴도치가 물을 만난경우
            elif type == PET and board[r][c] == PET: continue # 고슴도치가 이미 방문한 지역인 경우
            elif type == WATER and board[r][c] == 'D': continue # 물은 도착지점을 덮을 수 없다.
            elif type == WATER and board[r][c] == WATER: continue # 이미 물인 지역은 확장하지 않는다.
        
            elif type == PET and board[r][c] == 'D': return cost # 고슴도치가 잘 도착한 경우
        
            board[r][c] = type
            q.append((type, cost+1, r, c))
        
    return -1

if __name__ == "__main__":
    R, C = map(int, input().split())
    
    board = [ list(input()) for _ in range(R) ]

    sr, sc = -1, -1 # 시작지점
    for r in range(R):
        for c in range(C):
            if board[r][c] == 'S':
                sr, sc = r, c
            elif board[r][c] == '*':
                q.append((WATER, 1, r, c))
    q.append((PET, 1, sr, sc))
    
    ret = bfs()
    print("KAKTUS" if ret == -1 else ret)