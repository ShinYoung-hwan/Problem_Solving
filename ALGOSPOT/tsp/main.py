import sys

input = lambda: sys.stdin.readline().rstrip()

def DFS(cur=1, cost=0, path=[1]):
    global graph, ans, ans_path, visited, to_visit
    print(path)
    
    # base
    if to_visit == 0 and graph[cur][1] != 0:
        if ans > cost + graph[cur][1]:
            ans = cost + graph[cur][1]
            ans_path = path.copy()
        return
    
    # default
    for next, dist in enumerate(graph[cur]):
        if dist == 0: continue # 경로가 없는 경우
        if visited[next]: continue # 이미 방문한 경우
        if cost + dist > ans: continue
        
        visited[next] = True
        to_visit -= 1
        path.append(next)
        DFS(next, cost+dist, path)
        path.pop()
        to_visit += 1
        visited[next] = False
    
if __name__ == "__main__":
    N, M = map(int, input().split()) # 정점의 수: N, 간선의 수: M
    
    graph = [ [ 0 ] * (N+1) for _ in range(N+1) ]
    for _ in range(M):
        u, v, c = map(int, input().split())
        graph[u][v] = c
    print(graph)

    ans = sys.maxsize
    ans_path = []
    visited = [ False ] * (N+1)
    visited[1] = True # for start idx
    to_visit = N - 1
    
    DFS()
    
    if ans_path:
        print(ans)
        print(*ans_path)
    else:
        print(-1)