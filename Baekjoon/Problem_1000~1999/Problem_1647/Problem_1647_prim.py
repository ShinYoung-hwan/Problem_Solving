import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

def prim(graph, n):
    heap = []
    visited = [ False ] * (n+1)
    heapq.heappush(heap, (0, 1)) # 임이의 정점
    
    res = [] # 최소 스패닝 트리에 있는 간선 가중치 정보들
    cnt = 0 # 최소 스패닝 트리에 추가된 정점의 개수
    while heap:
        if cnt == n: break
        cur_weight, cur = heapq.heappop(heap)
        
        if visited[cur]: continue # 만약 방문했으면 다른 경로 확인
        
        for next, next_weight in graph[cur]:
            heapq.heappush(heap, (next_weight, next))
            
        visited[cur] = True
        res.append(cur_weight)
        cnt += 1
    
    return res

if __name__ == "__main__":
    n, m = map(int, input().split()) # 집의 개수 n, 길의 개수 m
    
    graph = [ [] for _ in range(n+1) ]
    for _ in range(m):
        a, b, c = map(int, input().split()) # 가중 길 (a, b, c)
        graph[a].append((b, c))
        graph[b].append((a, c))
        
    res = prim(graph, n)
    
    res[res.index(max(res))] = 0
    print(sum(res))