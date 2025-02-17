import sys
import heapq
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N, K = map(int, input().split()) # 보석의 개수 N, 가방의 수 K
    
    jewels = [ tuple(map(int, input().split())) for _ in range(N) ] # 각 보석의 (무게 M, 가치 V)
    jewels = deque(sorted(jewels))
    
    bags = [ int(input()) for _ in range(K) ] # 각 가방에 담을 수 있는 (무게 C)
    bags.sort()
    
    # solve
    ans = 0
    candidates = [] # 가장 높은 가치를 갖는 후보 heap
    for C in bags: # 각 가방에 담을 수 있는 (무게 C)
        while jewels and jewels[0][0] <= C:
            _, V = jewels.popleft()
            heapq.heappush(candidates, -V)
        if candidates: # 최적의 후보
            ans += -heapq.heappop(candidates)
    
    print(ans)