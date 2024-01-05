import sys, math
import heapq

input = lambda : sys.stdin.readline().rstrip()      
inputs = lambda : sys.stdin.readlines()

def dijkstra(graph, dist, x):
    # x에서 n개의 마을로 가는 최단시간 구하기
    heap = []
    heapq.heappush(heap, (0, x))
    dist = [ math.inf ] * (n+1)
    dist[x] = 0
    
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
    n, m, x = map(int, input().split()) # n명의 학생, n개의 마을, m개의 단방향도로, x 마을에서 파티 열림
    
    graph = [ list() for _ in range(n+1) ] # (갈수있는 마을, 이동 시간)
    for _ in range(m):
        # m개의 단방향 도로
        start, end, t = map(int, input().split())
        graph[start].append((end, t))
    
    results = [[]] # i 마을에서 각 집으로가는 시간
    for i in range(1, n+1):
        results.append((dijkstra(graph, n, i)))
    time_list = [0, ]
    for i in range(1, n+1):
        time_list.append((results[i][x]+results[x][i]))
    print(max(time_list))