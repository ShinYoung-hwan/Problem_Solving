import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

dr = [ -1, 1, 0, 0 ]
dc = [ 0, 0, -1, 1 ]

def BFS(r0, c0, visited, schedules):
    queue = deque()
    queue.append((r0, c0))
    visited[r0][c0] = True
    
    while queue:
        r0, c0 = queue.popleft()
        
        cnt_sea = 0
        for i in range(4):
            r, c = r0 + dr[i], c0 + dc[i]
            
            if heights[r][c] == 0:
                cnt_sea += 1
                continue
            elif visited[r][c]: continue
            
            queue.append((r, c))
            visited[r][c] = True
            
        if cnt_sea: schedules.append((r0, c0, cnt_sea))
        
def melt(schedules):
    global heights
    for r, c, a in schedules:
        heights[r][c] = max(0, heights[r][c] - a)
        
def solve():
    for y in range(0, sys.maxsize):
        cnt = 0
        visited = [ [ False ] * C for _ in range(R) ]
        schedules = [] # 매년 녹아야하는 빙하들의 정보 (r, c, amount)
        
        for r in range(1, R-1):
            for c in range(1, C-1):
                if heights[r][c] == 0: continue # 이미 빙하가 다 녹았다면 방문할 필요는 없다.
                if visited[r][c]: continue # 이미 방문했다면 추가로 방문할 필요는 없다.
                
                BFS(r, c, visited, schedules)
                cnt += 1

        if cnt > 1: return y
        elif cnt == 0: return 0
        melt(schedules)
                
    return 0

if __name__ == "__main__":
    R, C = map(int, input().split())
    heights = [ list(map(int, input().split())) for _ in range(R) ]
            
    print(solve())