import sys
import heapq
import math

input = lambda: sys.stdin.readline().rstrip()
inputs = lambda: sys.stdin.readlines()

def dijkstra(graph, n, src):
    dist = [ math.inf ] * (n+1)
    heap = []
    heapq.heappush(heap, (0, src))
    dist[src] = 0
    
    while heap:
        cur_cost, cur = heapq.heappop(heap)
        
        for next, next_weight in graph[cur]:
            next_cost = cur_cost + next_weight
            if dist[next] < next_cost: continue
            
            dist[next] = next_cost
            heapq.heappush(heap, (next_cost, next))
            
    return dist

if __name__ == "__main__":
    n = int(input()) # 노드의 개수
    
    graph = [ [] for _ in range(n+1) ]
    for u, v, w in [ map(int, edge.rstrip().split()) for edge in inputs() ]:
        graph[u].append((v, w))
        graph[v].append((u, w))
        
    dist = dijkstra(graph, n, 1)
    dist = dijkstra(graph, n, dist.index(max(dist[1:])))
    print(max(dist[1:]))