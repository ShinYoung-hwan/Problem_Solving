import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(grounds, visited, h0, r0, c0):
    queue = deque([(r0, c0)])
    visited[r0][c0] = True
    
    while queue:
        r0, c0 = queue.popleft()
        
        for i in range(4):
            r, c = r0 + dr[i], c0 + dc[i]
            
            if not ((0 <= r < N) and (0 <= c < N)): continue
            if grounds[r][c] <= h0: continue
            if visited[r][c]: continue
            
            queue.append((r, c))
            visited[r][c] = True

if __name__ == "__main__":
    N = int(input())
    grounds = []
    heights = set()
    
    for r in range(N):
        row = list(map(int, input().split()))
        
        for c in range(N):
            heights.add(row[c])
        grounds.append(row)
    
    answer = 1
    for height in sorted(heights):
        
        visited = [ [ False ] * N for _ in range(N) ]
        cnt = 0
        
        for r in range(N):
            for c in range(N):
                if grounds[r][c] <= height: continue
                if visited[r][c]: continue
                
                BFS(grounds, visited, height, r, c)
                cnt += 1
        
        answer = max(answer, cnt)
        
    print(answer)