import sys
import math
import heapq

SIZE = 100_001

input = lambda: sys.stdin.readline().rstrip()

def dijkstra(n, k):
    # n -> k로 이동하는 최단 경로의 걸리는 시간 구하기
    heap = []
    dist = [ math.inf ] * SIZE
    heapq.heappush(heap, (0, n))
    dist[n] = 0
    
    while heap:
        cur_cost, cur = heapq.heappop(heap)
        
        if dist[cur] < cur_cost: continue
        
        # 순간이동
        if (0 <= (next:=2*cur) < SIZE) and (dist[next] > cur_cost):
            dist[next] = cur_cost + 0
            heapq.heappush(heap, (cur_cost, next))
        
        # 좌우 이동
        for next in [ cur-1, cur+1 ]:
            if not (0 <= next < SIZE): continue
            
            if dist[next] > cur_cost + 1:
                dist[next] = cur_cost + 1
                heapq.heappush(heap, (cur_cost+1, next))
    
    return dist[k]    
    
if __name__ == "__main__":
    n, k = map(int, input().split()) # 시작점 n, 도착점 k
    
    print(dijkstra(n, k))