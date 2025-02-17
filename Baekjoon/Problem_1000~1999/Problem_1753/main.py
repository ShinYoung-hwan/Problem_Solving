import sys, math
import heapq

input = lambda: sys.stdin.readline().rstrip()

def dijkstra(graph, n, s):
    # 정점의 개수가 n인 방향 가중 그래프에서 s 정점을 시작으로 각 정점까지의 최단경로 구하기
    heap = [] # 다익스트라에서 힙 자료구조를 사용한다.
    dist = [ math.inf for _ in range(n+1) ] # 정점 s로부터 각 정점까지의 거리를 무한대로 초기화한다.
    
    heapq.heappush(heap, (0, s)) # 시작 정점을 삽입
    dist[s] = 0
    
    while len(heap):
        cur_dist, cur = heapq.heappop(heap)
        
        if dist[cur] < cur_dist: # 이미 최적화 경로이면 skip
            continue
        
        for next, weight in graph[cur]:
            next_dist = cur_dist + weight
            if dist[next] > next_dist: # 더 나은 경로이면 최신화
                dist[next] = next_dist
                heapq.heappush(heap, (next_dist, next))
    
    return dist

if __name__ == "__main__":
    v, e = map(int, input().split()) # 정점의 개수 v, 간선의 개수 e
    
    k = int(input()) # 시작 정점
    
    graph = [ [] for _ in range(v+1) ] # 방향 가중 그래프
    for _ in range(e):
        u1, u2, w = map(int, input().split()) # 가중치가 w인 u1 -> u2 간선
        graph[u1].append((u2, w))
    
    dist = dijkstra(graph, v, k)
    for i in range(1, v+1):
        print("INF" if dist[i] == math.inf else dist[i])
    