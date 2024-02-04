import sys
import heapq
import math

input = lambda: sys.stdin.readline().rstrip()

def dijkstra(graph, n, s):
    # s에서 각 정점으로 갈 때의 거리
    heap = []
    heapq.heappush(heap, (0, s))
    dist = [math.inf] * (n+1)
    dist[s] = 0
    
    while heap:
        weight, cur = heapq.heappop(heap)
        if dist[cur] < weight:
            continue
        
        for next, next_weight in graph[cur]:
            next_time = weight + next_weight
            if dist[next] > next_time:
                dist[next] = next_time
                heapq.heappush(heap, (next_time, next))
                
    for i in range(n+1):
        if dist[i] == math.inf:
            dist[i] = 0
                
    return dist[1:]

if __name__ == "__main__":
    n = int(input()) # 도시의 개수
    m = int(input()) # 버스의 개수
    
    graph = [ [] for _ in range(n+1) ] # 가중 그래프
    for _ in range(m):
        a, b, c = map(int, input().split()) # (a, b, c) a 도시 -> b 도시 cost c
        graph[a].append((b, c))
    
    for i in range(1, n+1):
        print(*dijkstra(graph, n, i))