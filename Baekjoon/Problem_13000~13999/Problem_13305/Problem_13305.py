import sys

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N = int(input()) # 도시의 개수
    D = list(map(int, input().split())) # i - (i+1) 도시 사이의 거리
    C = list(map(int, input().split())) # i번째 도시의 주유 cost
    
    ans = C[0] * D[0]
    min_cost = C[0]
    
    for i in range(1, N-1):
        min_cost = min(min_cost, C[i])
        ans += min_cost * D[i]
    
    print(ans)
