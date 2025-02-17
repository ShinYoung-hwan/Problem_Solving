import sys
import math
import heapq

input = lambda: sys.stdin.readline().rstrip()
inputs = lambda: sys.stdin.readlines()

def dijkstra(graph, n, src):
    # src에서 각 정점으로의 거리 구하기
    heap = []
    dist = [ math.inf ] * (n+1)
    heapq.heappush(heap, (0, src))
    dist[src] = 0
    
    while heap:
        cur_cost, cur = heapq.heappop(heap)
        
        if dist[cur] < cur_cost: continue
        
        for next, next_weight in graph[cur]:
            next_cost = cur_cost + next_weight
            if dist[next] > next_cost:
                dist[next] = next_cost
                heapq.heappush(heap, (next_cost, next))
    
    return  dist

if __name__ == "__main__": 
    n, m, x = map(int, input().split()) # 마을의 개수 n, 간선의 개수 m, 파티 진행 마을 x
    
    # 단방향 가중 그래프 저장
    go = [ [  ] for _ in range(n+1) ] # 정방향 그래프
    back = [ [  ] for _ in range(n+1) ] # 역방향 그래프
    for _ in range(m):
        u, v, t = map(int, input().split())
        go[u].append((v, t))
        back[v].append((u, t))
        
    # 각 마을에서 x를 지나 나시 본인마을로 오는 거리
    dist1 = dijkstra(go, n, x) # 각 마을에서 x로 가는 거리
    dist2 = dijkstra(back, n, x) # x에서 각 마을로 가는 거리
    print(max([ dist1[i] + dist2[i]  for i in range(1, n+1) ]))
    