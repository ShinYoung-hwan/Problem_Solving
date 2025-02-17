import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
isIn = lambda r, c: 0 <= r < H and 0 <= c < W 

dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]


def BFS(r0, c0, visited):
    queue = deque([(r0, c0)])
    visited[r0][c0] = True
    
    while queue:
        r0, c0 = queue.popleft()
        
        for i in range(8):
            r, c = r0 + dr[i], c0 + dc[i]
            
            if not isIn(r, c): continue
            if not ground[r][c]: continue
            if visited[r][c]: continue
            
            queue.append((r, c))
            visited[r][c] = True

if __name__ == "__main__":
    while True:
        W, H = map(int, input().split())
        if (W, H) == (0, 0): break
        
        ground = [ list(map(int, input().split())) for _ in range(H) ]
        
        visited = [ [ False ] * W for _ in range(H) ]
        cnt = 0
        
        for r in range(H):
            for c in range(W):
                if visited[r][c]: continue
                if not ground[r][c]: continue
                
                cnt += 1
                BFS(r, c, visited)
        
        print(cnt)

        