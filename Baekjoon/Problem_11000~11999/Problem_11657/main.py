import sys

INF = sys.maxsize
input = lambda: sys.stdin.readline().rstrip()

def bellman_ford(edges, n, src):
    # src에서 각 정점까지 방문할 수 최단 거리 확인 by bellman ford
    if n == 1: return [ -1 ] # 만약 도시의 개수가 1개인 경우
    
    dist = [ INF ] * (n+1)
    dist[src] = 0
    
    for v in range(n):
        for e in range(len(edges)):
            cur, next, weight = edges[e]
            if dist[cur] == INF: continue
            if dist[next] >  dist[cur] + weight:
                dist[next] = dist[cur] + weight
                if v == n-1: # 음의 순환이 있는 경우...
                    return [ -1 ]
    
    return dist[2:]
                
if __name__ == "__main__": 
    n, m = map(int, input().split()) # 도시의 개수 n, 버스 노선의 개수 m
    
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split()) # 버스 노선 (a, b, c)
        edges.append((a, b, c))
    
    for dist in bellman_ford(edges, n, 1):
        print(-1 if dist == INF else dist)