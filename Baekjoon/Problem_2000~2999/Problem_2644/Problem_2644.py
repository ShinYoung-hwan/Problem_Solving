import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def BFS(s, e):
    queue = deque()
    visited = [ -1 ] * (N+1)
    queue.append(s)
    visited[s] = 0
    
    while queue:
        cur = queue.popleft()
        
        for next in graph[cur]:
            if visited[next] >= 0: continue
            
            queue.append(next)
            visited[next] = visited[cur] + 1
            if next == e: return visited[e]
    
    return visited[e]

if __name__ == "__main__":
    N = int(input())
    s, e = map(int, input().split())
    
    M = int(input())
    graph = [ [] for _ in range(N+1) ]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    print(BFS(s, e))