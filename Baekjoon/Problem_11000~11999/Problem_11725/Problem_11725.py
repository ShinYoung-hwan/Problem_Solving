import sys

from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def bfs(graph, n):
    # bfs를 통해 부모 노드 찾기
    queue = deque()
    visited = [ -1 ] * (n+1)
    
    queue.append(1)
    visited[1] = 0
    
    while queue:
        cur = queue.popleft()
        
        for next in graph[cur]:
            if visited[next] >= 0: continue # 이미 방문한 노드
            
            visited[next] = cur
            queue.append(next)
    
    return visited

if __name__ == "__main__":
    n = int(input()) # 노드의 개수
    
    graph = [ [] for _ in range(n+1) ]
    
    for _ in range(n-1):
        u, v = map(int, input().split()) # u <-> v 간선
        graph[u].append(v)
        graph[v].append(u)
        
    parents = bfs(graph, n) # 각 노드의 부모노드 구하기
    
    for i in range(2, n+1):
        print(parents[i])