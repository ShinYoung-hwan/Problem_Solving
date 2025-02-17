import sys

from collections import deque

input = lambda: sys.stdin.readline().rstrip()
inputs = lambda: sys.stdin.readlines() 

def bfs(maps, m, n):
    # (0, 0)에서 (m-1, n-1)로 이동하는 최소 거리
    visited = [[[ -1, -1 ] for x in range(m)] for y in range(n) ]
    queue = deque()
    queue.append((0, 0, False))
    visited[0][0][False] = 1
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        x0, y0, is_broken = queue.popleft()
        
        if x0 == m-1 and y0 == n-1: # 목적지 도달
            return visited[y0][x0][is_broken]
        
        for i in range(4):
            x, y = x0 + dx[i], y0 + dy[i]
            
            if not (x in range(m) and y in range(n)): continue
            if visited[y][x][is_broken] >= 0: continue # 이미 방문했다면 다시 복귀
            
            if maps[y][x] == 0: # 일반적인 경로라면
                visited[y][x][is_broken] = visited[y0][x0][is_broken] + 1
                queue.append((x, y, is_broken))
            if maps[y][x] == 1 and not is_broken: # 벽을 부수고 가려고 할 때
                visited[y][x][not is_broken] = visited[y0][x0][is_broken] + 1
                queue.append((x, y, not is_broken))
    
    return -1
    
if __name__ == "__main__":
    n, m = map(int, input().split()) # maps의 크기, 가로 m, 세로 n
    maps = [ [ int(e) for e in line.rstrip() ] for line in inputs() ]
    
    print(bfs(maps, m, n))