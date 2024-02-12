import sys
import math
import heapq
input = lambda: sys.stdin.readline().rstrip()
inputs = lambda: sys.stdin.readlines()

def dijkstra(graph, n, src):
    # 정점의 개수가 n인 graph에서 src로부터 다른 지점까지의 거리
    dist = [ math.inf ] * (n+1)
    heap = []
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
    
    return dist
                
if __name__ == "__main__": 
    n, m, r = map(int, input().split()) # 지역 개수 n, 수색범위 m, 길의 개수 r
    nItems = [ 0 ] # 각 구역에 있는 아이템의 수
    nItems.extend(map(int, input().split()))
    
    graph = [ [] for _ in range(n+1) ]
    for _ in range(r):
        a, b, i = map(int, input().split()) # 길 (a, b, r)
        graph[a].append((b, i))
        graph[b].append((a, i))
    
    
    # 각 지점으로부터 다른 지점까지의 거리로 구하기
    res = 0
    for src in range(1, n+1):
        dist = dijkstra(graph, n, src)
        cur_item = 0
        for i in range(1, n+1):
            if dist[i] <= m:
                cur_item += nItems[i]
        res = max(res, cur_item)
    print(res)