import sys, math
import heapq

input = lambda: sys.stdin.readline().rstrip()   
inputs = lambda: sys.stdin.readlines()

def dijkstra(graph, n, s):
    # s에서 각 정점으로 갈 때의 거리
    heap = []
    heapq.heappush(heap, (0, s))
    dist = [math.inf] * (n+1)
    dist[s] = 0
    
    while len(heap):
        weight, cur = heapq.heappop(heap)
        if dist[cur] < weight:
            continue
        
        for next, next_weight in graph[cur]:
            next_time = weight + next_weight
            if dist[next] > next_time:
                dist[next] = next_time
                heapq.heappush(heap, (next_time, next))
                
    return dist

if __name__ == "__main__":
    n, e = map(int, input().split()) # n개의 정점, e개의 간선\
        
    graph = [ [] for _ in range(n+1) ] # 무방향 가중 그래프
    for _ in range(e):
        u, v, w = map(int, input().split()) # u - v, 가중치 w
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    v1, v2 = map(int , input().split()) # 꼭 지나야하는 정점 2개
    
    # 각 위치에서 각 정점으로 갈 때의 거리
    from_1 = dijkstra(graph, n, 1)
    from_v1 = dijkstra(graph, n, v1)
    from_v2 = dijkstra(graph, n, v2)
    
    # s -> v1 -> v2 -> e
    # s -> v2 -> v1 -> e
    res = min(from_1[v1]+from_v1[v2]+from_v2[n], from_1[v2]+from_v2[v1]+from_v1[n]) 
    print(-1 if res == math.inf else res)