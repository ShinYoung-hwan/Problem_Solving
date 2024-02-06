import sys
import math
import heapq

input = lambda: sys.stdin.readline().rstrip()

def dijkstra(graph, n, src, dest):
    heap = []
    dist = [ math.inf ] * (n+1)
    paths = [ [] for _ in range(n+1) ]
    dist[src] = 0
    paths[src] = [src]
    heapq.heappush(heap, (0, src, [src]))
    
    while heap:
        cur_cost, cur, cur_path = heapq.heappop(heap)
        
        if dist[cur] < cur_cost: # 이전 경로가 최선인 경우
            continue
        
        for next, weight in graph[cur]:
            next_cost = cur_cost + weight
            if dist[next] > next_cost: # 현재 경로가 최선인 경우
                cur_path.append(next)
                next_path = cur_path.copy()
                paths[next] = next_path
                heapq.heappush(heap, (next_cost, next, next_path))
                cur_path.pop()
                dist[next] = next_cost
    
    return dist[dest], paths[dest]
    
if __name__ == "__main__":
    n, m = int(input()), int(input()) # 도시의 개수 n, 버스의 개수 m
    
    graph = [ [ ] for _ in range(n+1) ] # 방향 가중 그래프
    for _ in range(m):
        u, v, c = map(int, input().split()) # 간선 (u, v, c)
        graph[u].append((v, c))
        
    a, b = map(int, input().split())
    # a -> b 로 이동하는 최단 경로 구하기
    
    cost, path = dijkstra(graph, n, a, b)
    
    print(cost)
    print(len(path))
    print(*path)
    