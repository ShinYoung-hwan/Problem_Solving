import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N = int(input())
    
    schedules = sorted([ tuple(map(int, input().split())) for _ in range(N) ])
    
    size = 0
    pq = [] # 현재 시각에 동시에 진행중인 회의들
    for schedule in schedules:
        while pq and pq[0] <= schedule[0]:
            heapq.heappop(pq)
        heapq.heappush(pq, schedule[1])
        size = max(size, len(pq))
        
    print(size)