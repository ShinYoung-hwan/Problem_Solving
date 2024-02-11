import sys
from copy import deepcopy
from collections import deque
from itertools import product, combinations

input = lambda: sys.stdin.readline().rstrip()
inputs = lambda: sys.stdin.readlines()

def bfs(lab, n, m, start: list):
    # 크기가 (n, m)인 lab에서 start에서 시작하는 bfs의 결과 구하기
    queue = deque(start)
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while queue:
        r0, c0 = queue.popleft()
        
        for i in range(4):
            r, c = r0 + dr[i], c0 + dc[i]
            
            if not ((0 <= r < n) and (0 <= c < m)): continue # 연구실 범위를 벗어남
            if lab[r][c] != 0: continue # 탐색 가능한 위치가 아닌 경우
            
            # 바이러스 확산
            queue.append((r, c))
            lab[r][c] = 2 
            
    return lab

if __name__ == "__main__": 
    n, m = map(int, input().split())
    lab = [ [ int(e) for e in line.split()] for line in inputs() ]
    
    # 바이러스 유포 위치 구하기
    start = []
    for r in range(n):
        for c in range(m):
            if lab[r][c] == 2:
                start.append((r, c))
    
    # 벽을 세우는 모든 경우 고려하기
    res = 0
    for (r1, c1), (r2, c2), (r3, c3) in combinations(product(range(n), range(m)), 3):
        # 만약 벽을 세울 위치가 빈 공간이 아니라면 ...
        if lab[r1][c1] != 0 or lab[r2][c2] != 0 or lab[r3][c3] != 0: continue
        
        # 벽 세우기
        lab[r1][c1], lab[r2][c2], lab[r3][c3] = 1, 1, 1
        
        # 바이러스 퍼트리기
        simulation_lab = bfs(deepcopy(lab), n, m, start)
        
        # 안전구역의 크기 구하기
        safe_zone = 0
        for r in range(n):
            for c in range(m):
                if simulation_lab[r][c] == 0:
                    safe_zone += 1
        res = max(res, safe_zone)
        
        # 벽 허물기
        lab[r1][c1], lab[r2][c2], lab[r3][c3] = 0, 0, 0
    
    print(res)