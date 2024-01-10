import sys, math
import heapq

input = lambda: sys.stdin.readline().rstrip()

def dijkstra(graph, n, dist, s):
    # 다익스트라 알고리즘
    heap = []
    heapq.heappush(heap, (0, s))
    
    while len(heap):
        cur_cost, cur = heapq.heappop(heap)
        if cur_cost > dist[cur]: continue # 
        
        for next, next_weight in graph[cur]:
            next_cost = cur_cost + next_weight
            if dist[next] > next_cost:
                dist[next] = next_cost
                heapq.heappush(heap, (next_cost, next))

if __name__ == "__main__":
    n, m = int(input()), int(input()) # 도시의 개수 n, 버스의 개수 m
    
    # 버스 정보
    graph = [ [] for _ in range(n+1) ]
    for _ in range(m):
        u, v, w = map(int, input().split()) # u -> v 
        graph[u].append((v, w))
        
    s, e = map(int, input().split())
    
    dist = [ math.inf ] * (n+1)
    dijkstra(graph, n, dist, s)
    print(dist[e])