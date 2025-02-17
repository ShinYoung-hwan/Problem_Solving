import sys

from collections import deque

input = lambda : sys.stdin.readline().rstrip()
inputs = lambda : sys.stdin.readlines()

def is_in_maps(x, y, n, m):
    return (0 <= x < m) and (0 <= y < n)

def get_target_pos(maps, n, m):
    # n*m 크기의 지도에서 target의 위치 구하기
    for y in range(n):
        for x in range(m):
            if maps[y][x] == 2:
                return x, y
            
def get_n_path(maps, n, m, x0, y0):
    # x0, y0에서 각 위치까지의 거리를 bfs를 이용해 구한다.
    paths = [ [ 0 if maps[y][x] == 0 else -1 for x in range(m) ] for y in range(n) ]
    visited = [ [False] * m for _ in range(n) ]
    queue = deque([(x0, y0, 0)])
    visited[y0][x0] = True
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while len(queue) > 0:
        tx, ty, path = queue.popleft()
        paths[ty][tx] = path
        
        for i in range(4):
            x, y = tx + dx[i], ty + dy[i]
            
            if not is_in_maps(x, y, n, m):
                continue
            if visited[y][x]:
                continue
            if maps[y][x] == 0:
                continue
            
            queue.append((x, y, path+1))
            visited[y][x] = True
    
    return paths
    
if __name__ == "__main__":
    n, m = map(int, input().split())
    maps = [ [ int(pos) for pos in line.split() ] for line in inputs() ]
    
    x, y = get_target_pos(maps, n, m)
    paths = get_n_path(maps, n, m, x, y)

    for line in paths:
        print(*line)