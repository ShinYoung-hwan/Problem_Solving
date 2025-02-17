import sys
import math
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
inputs = lambda: sys.stdin.readlines()
        

def get_start(spaces, n):
    for r in range(n):
        for c in range(n):
            if spaces[r][c] == 9:
                return r, c

def bfs(spaces, n, r0, c0, size):
    # bfs로 가장 가까운 잡아먹을 수 있는 위치 구하기
    queue = deque()
    visited = [ [ -1 ] * n for _ in range(n) ]
    queue.append((r0, c0))
    visited[r0][c0] = 0
    
    dr = [ -1, 0, 1, 0 ]
    dc = [ 0, -1, 0, 1 ]
    
    while queue:
        r0, tc = queue.popleft()
    
        for i in range(4):
            r, c = r0 + dr[i], tc + dc[i]
            
            if not ((0 <= r < n) and (0 <= c < n)): continue
            if visited[r][c] >= 0: continue
            if spaces[r][c] > size: continue
            
            visited[r][c] = visited[r0][tc] + 1
            queue.append((r, c))
            
    return visited

if __name__ == "__main__": 
    n = int(input()) # spaces의 크기 (n, n)
    spaces = [ [ int(e) for e in line.split() ] for line in inputs() ] 
    
    # 아기 상어의 위치 구하기
    r0, c0 = get_start(spaces, n)
    spaces[r0][c0] = 0
    
    size = 2 # 아기상어의 크기
    res = 0 # 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간
    
    # 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간을 구하기
    res = 0
    fish = 0
    while True:
        visited = bfs(spaces, n, r0, c0, size) # 현재 위치에서 각 위치로의 방문 시간

        # 좌측 상단부터 확인
        min_val = math.inf # 시간 최솟값
        for r in range(n):
            for c in range(n):
                if visited[r][c] == -1: continue # 이동불가구역
                if not (0 < spaces[r][c] < size): continue # 잡아 먹을 수 있는 경우가 아님
                if min_val <= visited[r][c]: continue # 더 짧은 거리가 아닌 경우
                
                min_val = visited[r][c]
                r0, c0 = r, c
        
        if math.isinf(min_val): break # 더이상 잡아 먹을 수 없음.
        
        spaces[r0][c0] = 0
        fish += 1
        res += min_val
        if fish >= size:
            size += 1
            fish = 0
                    
    print(res)